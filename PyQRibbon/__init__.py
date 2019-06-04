# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 13:22
# @Author  : llc
# @File    : __init__.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QToolBar
from .widgets import QRibbonWidget
from .widgets.frameless_window import FramelessWindow
import os


class QRibbonToolBar(QToolBar):
    def __init__(self, parent=None):
        super(QRibbonToolBar, self).__init__(parent)
        self.parent = parent

        if not isinstance(self.parent, FramelessWindow):
            raise TypeError("__init__(self, parent=None) 'parent' requires 'FramelessWindow' type.")

        self.setStyleSheet(open(os.path.join(os.path.dirname(__file__), 'qss/QRibbonWidget.qss')).read())

        self.ribbon_widget = QRibbonWidget(self)
        self.addWidget(self.ribbon_widget)
        self.setAllowedAreas(Qt.NoToolBarArea)
        self.setMovable(False)
        self.setFloatable(False)

        self.setMouseTracking(True)

        self.add_widget = self.ribbon_widget.title_bar.add_widget
        self.add_menu = self.ribbon_widget.menu_bar.add_menu
        self.add_group = self.ribbon_widget.menu_bar.add_group

        self.ribbon_widget.title_bar.button_min.clicked.connect(self.parent.showMinimized)
        self.ribbon_widget.title_bar.button_max.clicked.connect(self.show_max)
        self.ribbon_widget.title_bar.button_close.clicked.connect(self.parent.close)

    @property
    def title(self):
        return self.ribbon_widget.title_bar.title

    @title.setter
    def title(self, title):
        self.ribbon_widget.title_bar.set_title(title)

    def show_max(self):
        if self.ribbon_widget.title_bar.button_max.text() == '1':
            self.ribbon_widget.title_bar.button_max.setText('2')
            self.parent.showMaximized()
        else:
            self.ribbon_widget.title_bar.button_max.setText('1')
            self.parent.showNormal()
