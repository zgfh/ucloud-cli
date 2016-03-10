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
        print "\"tag='test',name='test',password='dangerous',cpu='1',memory=2,diskSpace='50',imageId='uimage-x1yary',uhostType='Normal'\" \neg:  "+sys.argv[0]+ " \"'test','test',password='dangerous'\" "
        exit(1)

    eval ("host.create("+sys.argv[1]+")")