#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 17/4/8 下午12:27
"""
import cdn_utils,sys

if __name__ == '__main__':
    arg_length = len(sys.argv)
    if arg_length < 3:
        print "eg:  "+sys.argv[0]+ "  DomainId  url_dir"
        print "eg:  "+sys.argv[0]+ "  ucdn-xxx  http://daohub-ufile-driver-test/"
        exit(1)
    #print  sys.argv
    result=cdn_utils.flush_cdn(sys.argv[1],sys.argv[2])
    if result==False:
        exit(-1)