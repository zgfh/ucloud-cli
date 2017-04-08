#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 17/4/8 上午11:40
"""

from sdk import UcloudApiClient

from config import *
import time

def flush_task_status_cdn(DomainId,TaskId):
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "DescribeRefreshCacheTask",
        "Region": region,
        "Zone":zone,
        "ProjectId":project_id,
        "DomainId": DomainId,
        "TaskId": TaskId
    }
    response = ApiClient.get("/", Parameters)
    if 0 != response['RetCode']:
        print response
        exit(1)
    return response['TaskSet'][0]['Status']


def flush_cdn(DomainId,UrlList,Type='dir'):
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters = {
        "Action": "RefreshUcdnDomainCache",
        "Region": region,
        "Zone":zone,
        "ProjectId":project_id,
        "DomainId": DomainId,
        "Type": Type,
        "UrlList.0": UrlList
    }
    response = ApiClient.get("/", Parameters)
    if 0 != response['RetCode']:
        print response
        exit(1)
    print response
    taskId=response['TaskId']
    for i in range(1200):
        status=flush_task_status_cdn(DomainId,taskId)
        print status
        if status=="success":
            return True
        elif status=="failure":
            return False
        time.sleep(1)
    return False



if __name__ == '__main__':
    pass