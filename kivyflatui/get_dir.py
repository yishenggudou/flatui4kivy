#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    Copyright 2011 timger
#    +Author timger
#    +Gtalk&Email yishenggudou@gmail.com
#    +Msn yishenggudou@msn.cn
#    +Weibo @timger http://t.sina.com/zhanghaibo
#    +twitter @yishenggudou http://twitter.com/yishenggudou
#    Licensed under the MIT License, Version 2.0 (the "License");



def get_dir():
    import os
    DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
    NAME_FILE = os.path.relpath(__file__)
    return DIR_PATH
