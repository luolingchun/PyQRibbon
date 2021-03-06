# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 9:30
# @Author  : llc
# @File    : __init__.py.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from .widgets import TitleBar, MenuBar, GroupWidget


class QRibbonWidget(QWidget):
    def __init__(self, parent=None):
        super(QRibbonWidget, self).__init__(parent)

        self.title_bar = TitleBar(self)
        self.menu_bar = MenuBar(self)

        vl = QVBoxLayout(self)
        vl.setContentsMargins(0, 0, 0, 0)
        vl.setSpacing(0)
        vl.addWidget(self.title_bar)
        vl.addWidget(self.menu_bar)

        self.setMouseTracking(True)
