# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 13:15
# @Author  : llc
# @File    : widgets.py
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy, QLabel, QHBoxLayout, QPushButton


class QRibbonTitleBar(QWidget):
    def __init__(self, parent=None):
        super(QRibbonTitleBar, self).__init__(parent)

        self._main_window = parent.parent
        self._title = 'no title'

        self._init()

        font = QFont("Webdings")
        # close
        self._label_close = QPushButton('r')
        self._label_close.setFont(font)
        self._label_close.clicked.connect(self._main_window.close)
        self.add_widget(self._label_close, left=False)
        # max
        self._label_max = QPushButton('1')
        self._label_max.setFont(font)
        self._label_max.clicked.connect(self._main_window_showMaximized)
        self.add_widget(self._label_max, left=False)
        # min
        self._label_min = QPushButton('0')
        self._label_min.setFont(font)
        self._label_min.clicked.connect(self._main_window.showMinimized)
        self.add_widget(self._label_min, left=False)

    def _init(self):
        hl = QHBoxLayout(self)
        hl.setContentsMargins(0, 0, 0, 0)
        l_widget = QWidget()
        self._l_hl = QHBoxLayout(l_widget)
        self._l_hl.setContentsMargins(0, 0, 0, 0)
        hl.addWidget(l_widget)
        hs_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hl.addSpacerItem(hs_l)
        self._label_title = QLabel(self._title)
        hl.addWidget(self._label_title)
        hs_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hl.addSpacerItem(hs_r)
        r_widget = QWidget()
        self._r_hl = QHBoxLayout(r_widget)
        self._r_hl.setContentsMargins(0, 0, 0, 0)
        hl.addWidget(r_widget)

    def _main_window_showMaximized(self):
        if not self._main_window.isMaximized():
            self._main_window.showMaximized()
            self._label_max.setText('2')
        else:
            self._main_window.showNormal()
            self._label_max.setText('1')

    def set_title(self, title):


        self._title = title
        self._label_title.setText(self._title)

    def add_widget(self, widget, left=True):
        if left:
            self._l_hl.insertWidget(-1, widget)
        else:
            self._r_hl.insertWidget(0, widget)
