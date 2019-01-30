# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 13:15
# @Author  : llc
# @File    : widgets.py
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel, QHBoxLayout, QPushButton, QTabWidget, QTabBar


class BaseWidget(QWidget):
    def __init__(self, *args):
        super(BaseWidget, self).__init__(*args)


class TitleButton(QPushButton):
    def __init__(self, *args):
        super(TitleButton, self).__init__(*args)
        _font = QFont("Webdings")
        _font.setPointSize(12)
        self.setFont(_font)


class TitleWidget(QPushButton):
    def __init__(self, *args):
        super(TitleWidget, self).__init__(*args)


class TabBar(QTabBar):
    def __init__(self, *args):
        super(TabBar, self).__init__(*args)


class TitleBar(QWidget):
    def __init__(self, parent=None):
        super(TitleBar, self).__init__(parent)

        self._title = 'no title'

        self._init_ui()

        # close
        self.button_close = TitleButton('r')
        self.button_close.setObjectName('ButtonClose')
        self._r_hl.insertWidget(0, self.button_close)
        # max
        self.button_max = TitleButton('1')
        self.button_max.setObjectName('ButtonMax')
        self._r_hl.insertWidget(0, self.button_max)
        # min
        self.button_min = TitleButton('0')
        self.button_min.setObjectName('ButtonMin')
        self._r_hl.insertWidget(0, self.button_min)

    def _init_ui(self):
        hl = QHBoxLayout(self)
        hl.setContentsMargins(0, 0, 0, 0)
        hl.setSpacing(0)
        l_widget = BaseWidget()
        self._l_hl = QHBoxLayout(l_widget)
        self._l_hl.setContentsMargins(0, 0, 0, 0)
        self._l_hl.setSpacing(0)
        hl.addWidget(l_widget)
        hl.setContentsMargins(0, 0, 0, 0)
        self._label_title = QLabel(self._title)
        self._label_title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self._label_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        hl.addWidget(self._label_title)
        r_widget = BaseWidget()
        self._r_hl = QHBoxLayout(r_widget)
        self._r_hl.setContentsMargins(0, 0, 0, 0)
        self._r_hl.setSpacing(0)
        hl.addWidget(r_widget)

    def set_title(self, title):
        if not isinstance(title, str):
            raise TypeError("'title' requires 'str' type.")
        self._title = title
        self._label_title.setText(self._title)

    def add_widget(self, icon, left=True):
        if not isinstance(icon, str):
            raise TypeError("'icon' requires 'str' type.")
        widget = TitleWidget()
        widget.setIcon(QIcon(icon))
        if left:
            self._l_hl.insertWidget(-1, widget)
        else:
            self._r_hl.insertWidget(0, widget)


class TabMenuBar(QTabWidget):
    def __init__(self, parent=None):
        super(TabMenuBar, self).__init__(parent)
        _tab_bar = TabBar()
        self.setTabBar(_tab_bar)

    def add_tab(self, p_str):
        _tab = BaseWidget()
        self.addTab(_tab, p_str)


class GroupWidget(QWidget):
    def __init__(self, parent=None):
        super(GroupWidget, self).__init__(parent)
