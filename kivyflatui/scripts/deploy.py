#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    Copyright 2011 timger
#    +Author timger
#    +Gtalk&Email yishenggudou@gmail.com
#    +Msn yishenggudou@msn.cn
#    +Weibo @timger http://t.sina.com/zhanghaibo
#    +twitter @yishenggudou http://twitter.com/yishenggudou
#    Licensed under the MIT License, Version 2.0 (the "License");


import os
import sys

DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
NAME_FILE = os.path.relpath(__file__)
sys.path.append(os.path.join(DIR_PATH,'..','kivyflatui'))

from fabric.api import *
from conf import conf
svn_dir="/data/"
env.hosts = ['root@{host}'.format(host=host) for host in conf['ngxlog']]
env.password = 'letv2011@ops'

print env.hosts

def deploy():
    with cd(svn_dir):
        run('uname -a')
