# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 13:22
# @Author  : llc
# @File    : __init__.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QToolBar, QMainWindow
from .widgets import QRibbonTitleBar


class QRibbonWidget(QToolBar):

    def __init__(self, parent=None):
        super(QRibbonWidget, self).__init__(parent)
        self.parent = parent

        self._init()

    def _init(self):
        if not self.parent or not isinstance(self.parent, QMainWindow):
            raise TypeError(f'__init__(self, parent=None): argument 1 has unexpected type {type(self.parent)}')

        self._title_bar = QRibbonTitleBar(self)
        self.addWidget(self._title_bar)
        self.setAllowedAreas(Qt.TopToolBarArea)
        self.setMovable(False)
        self.setFloatable(False)

        self.parent.addToolBar(self)

    def title_bar(self):
        return self._title_bar

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.globalPos()
            print(self.start_point)
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            diff_point=event.globalPos()-self.start_point
            print(diff_point,self.start_point)
            self.parent.move(self.parent.pos() + diff_point)
            event.accept()
