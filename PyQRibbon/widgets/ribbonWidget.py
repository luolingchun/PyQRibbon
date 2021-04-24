# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/4/10 16:36
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QSizePolicy, QTabWidget, QFrame

from PyQRibbon.utils import create_layout


class QBaseWidget(QFrame):
    """基础控件"""

    def __init__(self, parent=None):
        super(QBaseWidget, self).__init__(parent)
        # 鼠标追踪
        self.setMouseTracking(True)


class QTitleButton(QPushButton):
    """标题栏按钮：最小化、最大化、关闭按钮"""

    def __init__(self, *args, **kwargs):
        super(QTitleButton, self).__init__(*args, **kwargs)
        # 鼠标追踪
        self.setMouseTracking(True)


class QFileButton(QPushButton):
    """分组中文件按钮：file"""

    def __init__(self, *args, **kwargs):
        super(QFileButton, self).__init__(*args, **kwargs)
        # 鼠标追踪
        self.setMouseTracking(True)


class QTitleLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(QTitleLabel, self).__init__(*args, **kwargs)
        # 鼠标追踪
        self.setMouseTracking(True)


class QTitleWidget(QBaseWidget):
    """标题栏控件"""

    def __init__(self, parent=None):
        super(QTitleWidget, self).__init__(parent)

        self._title = 'xxx'

        self.__init_ui()

    def __init_ui(self):
        # 标题栏横向布局
        hl = create_layout(self)
        # 标题栏左侧按钮布局：保存、打印...
        self._lhl = create_layout()
        hl.addLayout(self._lhl)
        # 标题栏标题
        self.titleLabel = QTitleLabel(self.title, self)
        # 水平居中
        self.titleLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # 横向扩展，纵向最小
        self.titleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        hl.addWidget(self.titleLabel)
        # 标题栏右侧按钮布局：最小化、最大化、关闭按钮...
        self._rhl = create_layout()
        hl.addLayout(self._rhl)

        # 关闭按钮
        self.closeButton = QTitleButton('🗙', self)
        self.closeButton.setObjectName('closeButton')
        self.addRightWidget(self.closeButton)
        # 最大化按钮
        self.maxButton = QTitleButton('🗖', self)
        self.maxButton.setObjectName('maxButton')
        self.addRightWidget(self.maxButton)
        # 最小化按钮
        self.minButton = QTitleButton('⎯', self)
        self.minButton.setObjectName('minButton')
        self.addRightWidget(self.minButton)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        self.titleLabel.setText(title)

    def addLeftWidget(self, widget: QWidget):
        """在标题栏左侧添加控件"""
        self._lhl.insertWidget(-1, widget)

    def addRightWidget(self, widget: QWidget):
        """在标题栏右侧添加控件"""
        self._rhl.insertWidget(0, widget)


class QGroupPanel(QTabWidget):
    def __init__(self, parent=None):
        super(QGroupPanel, self).__init__(parent)
        # 左侧文件按钮
        self.fileButton = QFileButton('文件', self)
        self.setCornerWidget(self.fileButton, corner=Qt.TopLeftCorner)

        self.setMouseTracking(True)

        self.currentChanged.connect(lambda: self.setStyleSheet(""))


class QRibbonWidget(QFrame):
    def __init__(self, parent=None):
        super(QRibbonWidget, self).__init__(parent)
        # 标题组件
        self.titleWidget = QTitleWidget(self)
        # 分组组件
        self.groupPanel = QGroupPanel(self)
        # 创建垂直布局
        vl = create_layout(self, direction='v')
        vl.addWidget(self.titleWidget)
        vl.addWidget(self.groupPanel)

        self.setMouseTracking(True)
