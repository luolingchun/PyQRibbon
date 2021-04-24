# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/4/10 16:53

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


def create_layout(parent=None, direction='h'):
    """创建横向、纵向布局"""
    layout = None
    if direction == 'h':
        layout = QHBoxLayout(parent)
    elif direction == 'v':
        layout = QVBoxLayout(parent)
    if layout is not None:
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
    return layout
