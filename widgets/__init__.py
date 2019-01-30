# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 9:30
# @Author  : llc
# @File    : __init__.py.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from .widgets import TitleBar, TabMenuBar, GroupWidget


class _QRibbonWidget(QWidget):
    def __init__(self, ribbonwindow=None):
        super(_QRibbonWidget, self).__init__()
        self._ribbonwindow = ribbonwindow

        self.title_bar = TitleBar(self)
        self.title_bar.button_close.clicked.connect(self._ribbonwindow.close)
        self.title_bar.button_max.clicked.connect(self._ribbonwindow_showMaximized)
        self.title_bar.button_min.clicked.connect(self._ribbonwindow.showMinimized)
        self._ribbonwindow.double_click.connect(self._ribbonwindow_showMaximized)

        self.tabmenu_bar = TabMenuBar(self)
        #
        # self.group_widget = GroupWidget(self)

        self._init_ui()

    def _init_ui(self):
        _vl = QVBoxLayout(self)
        _vl.setContentsMargins(0, 0, 0, 0)
        _vl.setSpacing(0)
        _vl.addWidget(self.title_bar)

        _vl.addWidget(self.tabmenu_bar)

        # _vl.addWidget(self.group_widget)

    def _ribbonwindow_showMaximized(self):
        if not self._ribbonwindow.isMaximized():
            self._ribbonwindow.showMaximized()
            self.title_bar.button_max.setText('2')
        else:
            self._ribbonwindow.showNormal()
            self.title_bar.button_max.setText('1')
