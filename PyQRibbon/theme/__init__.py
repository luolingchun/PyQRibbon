# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/4/5 15:35
import os

_here = os.path.dirname(__file__)

default = open(os.path.join(_here, 'default.qss'), 'r', encoding='utf8').read()

foldIcon = os.path.join(_here, 'images', 'fold.png')
fixedIcon = os.path.join(_here, 'images', 'fixed.png')
