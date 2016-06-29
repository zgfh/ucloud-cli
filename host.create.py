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
    arg_length = len(sys.argv)
    if arg_length < 2:
        print """
           ./host.create.py tag name password cpu momory diskSpace imageId uhostType
        eg:
            ./host.create.py test test dangerous 1 2 100
            ./host.create.py test test2 dangerous 2 4 100 uimage-x1yary SATA_SSD

        option
        imageId:
           uimage-x1yary: ubuntu14.04

        uhostType:
            Normal,SATA_SSD,BigData
        """
        exit(1)

    host_utils.create(*sys.argv[1:])