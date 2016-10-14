#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 16/3/7 上午11:10
"""
import base64
import json
import time,sys

from sdk import UcloudApiClient

from config import *


def create(tag='',Bandwidth=2,ChargeType='Dynamic',PayMode='Traffic'):
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "AllocateEIP",
        "Region": region,
        "OperatorName": 'Bgp',
        "Bandwidth": Bandwidth,
        "ChargeType": ChargeType,
        "PayMode": PayMode,
        "Tag": tag,
        "Remark": 'ip_Remark'
    }
    response = ApiClient.get("/", Parameters)
    #print response
    if 0 != response['RetCode']:
        print response
        exec (1)
    #print response

    if 'EIPSet' in response  :
        return  response['EIPSet'][0]['EIPAddr'][0]['IP']

    raise TypeError("can not get host info")


def get_all(resourceType=None):
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "DescribeEIP",
        "Region": region,
        "Limit": '100000'
    }
    ips = ApiClient.get("/", Parameters)
    #print ips
    result_ips=[]
    for ip_tmp in ips['EIPSet']:
        if  resourceType and resourceType == ip_tmp['Resource']['ResourceType']:
            result_ips.append( ip_tmp['EIPAddr'][0]['IP'])
        elif resourceType is None:
            result_ips.append( ip_tmp['EIPAddr'][0]['IP'])
    return result_ips


def get(ip=None,tag=None):
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "DescribeEIP",
        "Region": region,
        "Limit": '100000'
    }
    ips = ApiClient.get("/", Parameters)
    #print ips
    for ip_tmp in ips['EIPSet']:
        if ip and  ip == ip_tmp['EIPAddr'][0]['IP'] :
            return ip_tmp
        if tag and tag == ip_tmp['Tag'] :
            return ip_tmp

def bind(ip,hostId):
    ip = get(ip)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "BindEIP",
        "Region": region,
        'ResourceType':'uhost',
        'ResourceId':hostId, #TODO
        "EIPId": ip['EIPId']
    }
    response = ApiClient.get("/", Parameters);

    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))

def unbing(ip,hostId):
    ip = get(ip)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "UnBindEIP",
        "Region": region,
        'ResourceType':'uhost',
        'ResourceId':hostId, #TODO
        "EIPId": ip['EIPId']
    }
    response = ApiClient.get("/", Parameters);

    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))

def modify_eip_weight(ip,weight=50):
    ip = get(ip)
    print 'start modify_eip_weight {} to weight{} '.format(ip,weight)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "ModifyEIPWeight",
        "Region": region,
        'Weight':weight,
        "EIPId": ip['EIPId']
    }
    response = ApiClient.get("/", Parameters);

    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))


def delete(ip):
    ip = get(ip)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "ReleaseEIP",
        "Region": region,
        "EIPId": ip['EIPId']
    }
    response = ApiClient.get("/", Parameters);

    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))

def change_out_ip(old_ip,hostId):
    time_tip=int(1)
    ip=create()
    time.sleep(time_tip)
    print "change ip to :{}".format(ip)
    print 'bind ip {}'.format(ip)
    bind(ip,hostId)
    time.sleep(time_tip)
    time.sleep(time_tip)

    if old_ip:
        print 'modify_eip_weight ip {} to 60'.format(old_ip)
        modify_eip_weight(old_ip,60)
        time.sleep(time_tip)
        print 'unbing old ip {}'.format(old_ip)
        unbing(old_ip,hostId)
        delete(old_ip)
        time.sleep(time_tip)

    modify_eip_weight(ip,100)
    if len(get_all())>2:
        raise Exception(' too ip mach')
    return ip

if __name__ == '__main__':
    #ip='106.75.6.161'
    #ip=create('test2')
    #print ip
    #print get(ip)
    #print get(tag='test2')
    #delete(ip)
    #bind(ip)
    #print get_all(resourceType='vrouter')
    #unbing(ip)
    #modify_eip_weight('106.75.10.75',5)
    #change_ip()
    #change_out_ip('106.75.7.211','uhost-xv2qrp')
    #change_ip('106.75.8.30','uhost-xv2qrp')
    #deal_err('106.75.11.233','uhost-xv2qrp')
    #change_ip('uhost-xv2qrp')
    pass
