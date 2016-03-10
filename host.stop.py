#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 16/3/10 下午1:02
"""
import host
import sys

if __name__ == '__main__':
    arg_length = len(sys.argv)
    if arg_length < 2:
        print "eg:  "+sys.argv[0]+ "  10.10.10.10"
        exit(1)
    #print  sys.argv
    for ip in sys.argv[1:]:
        host.stop(ip)