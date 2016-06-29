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
import time

from sdk import UcloudApiClient

from config import *


def create(tag=None, name=None, password='dangerous', cpu='1', memory=2, diskSpace='50', imageId="uimage-j4fbrn",
           uhostType='Normal'):
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "CreateUHostInstance",
        "Region": region,
        "ImageId": imageId,
        "LoginMode": "Password",
        "Password": base64.b64encode(password),
        "Tag": tag,
        "CPU": cpu,
        "Memory": int(memory) * 1024,
        "DiskSpace": diskSpace,
        "Name": name,
        "UHostType": uhostType  # SATA_SSD ,BigData

    }
    response = ApiClient.get("/", Parameters)
    if 0 != response['RetCode']:
        print response
        exec (1)

    for i in range(120):
        time.sleep(1)
        host = get(name)
        if host and 'IPSet' in host and 'IP' in host['IPSet'][0]:  # and 'Running' in host['State']
            print host['IPSet'][0]['IP']
            return host
    raise TypeError("can not get host info")


def get_all():
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "DescribeUHostInstance",
        "Region": region,
        "Limit": '100000'
    }
    response = ApiClient.get("/", Parameters);

    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))


def get(host_name='', ip=''):
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "DescribeUHostInstance",
        "Region": region,
        "Limit": '100000'
    }
    hosts = ApiClient.get("/", Parameters)

    for host in hosts['UHostSet']:
        if host_name == host['Name'] or ip == host['IPSet'][0]['IP']:
            return host


def stop(ip, check=False):
    host = get(ip=ip)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "StopUHostInstance",
        "Region": region,
        "UHostId": host['UHostId']
    }
    response = ApiClient.get("/", Parameters);
    if check:
        checkStatus(ip, 'Stopped')

    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))


def poweroff(ip, check=False):
    host = get(ip=ip)

    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "PoweroffUHostInstance",
        "Region": region,
        "UHostId": host['UHostId']
    }
    response = ApiClient.get("/", Parameters);
    if check:
        checkStatus(ip, 'Stopped')

    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))


"""
status :Running ,Stopping
"""


def checkStatus(ip, status='Running'):
    host = get(ip=ip)
    for i in range(120):
        host = get(ip=ip)
        print host['State']
        if status in host['State']:
            return
        time.sleep(1)
    exit(1)


def reboot(ip, check=False):
    host = get(ip=ip)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "RebootUHostInstance",
        "Region": region,
        "UHostId": host['UHostId']
    }
    response = ApiClient.get("/", Parameters);
    if check:
        checkStatus(ip)

    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))


def ReinstallUHostInstance(ip, password='dangerous', imageId='uimage-j4fbrn'):
    host = get(ip=ip)
    poweroff(ip, check=True)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "ReinstallUHostInstance",
        "Region": region,
        "UHostId": host['UHostId'],
        "Password": base64.b64encode(password),
        "ImageId": imageId
    }
    response = ApiClient.get("/", Parameters);

    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))


def delete(ip):
    host = get(ip=ip)
    stop(ip, check=True)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "TerminateUHostInstance",
        "Region": region,
        "UHostId": host['UHostId']
    }
    response = ApiClient.get("/", Parameters);

    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    # create('test','test','dangerous',2,4,200)
    pass
