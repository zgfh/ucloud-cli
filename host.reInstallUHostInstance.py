#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 16/3/10 下午1:02
"""
import host_utils
import sys

if __name__ == '__main__':
    imageId="uimage-j4fbrn"
    arg_length = len(sys.argv)
    if arg_length < 3:
        print "eg: "+sys.argv[0]+ " password ip image_id\neg:  "+sys.argv[0]+ " dangerous  10.10.10.10 uimage-j4fbrn"
        exit(1)
    if arg_length >=4:
        imageId=sys.argv[3]
    #print  sys.argv
    for ip in sys.argv[2:]:
        host_utils.ReinstallUHostInstance(ip, password=sys.argv[1], imageId=imageId)