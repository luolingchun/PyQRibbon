# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 13:22
# @Author  : llc
# @File    : __init__.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QToolBar

from PyQRibbon.theme import default
from PyQRibbon.widgets.framelessWindow import FramelessWindow
from PyQRibbon.widgets.ribbonWidget import QRibbonWidget, QLabel


class QRibbonWindow(FramelessWindow):
    def __init__(self, style='default'):
        super(QRibbonWindow, self).__init__()
        self.style = style
        self.setObjectName('QRibbonWindow')

        # 设置样式
        if self.style == 'default':
            self.setStyleSheet(default)
        # 添加工具栏
        toolBar = QToolBar(self)
        toolBar.setMouseTracking(True)
        self.ribbonWidget = QRibbonWidget(toolBar)
        toolBar.addWidget(self.ribbonWidget)
        toolBar.setAllowedAreas(Qt.NoToolBarArea)
        toolBar.setMovable(False)
        toolBar.setFloatable(False)
        self.addToolBar(toolBar)
        # 添加中心控件
        self.centralWidget = QWidget(self)
        self.centralWidget.setMouseTracking(True)
        self.centralWidget.setObjectName("centralWidget")
        self.setCentralWidget(self.centralWidget)
        # 安装时间过滤器
        self.installEventFilter(self)
        self.ribbonWidget.groupPanel.installEventFilter(self)
        self.minButton.installEventFilter(self)
        self.maxButton.installEventFilter(self)
        self.closeButton.installEventFilter(self)
        self.fileButton.installEventFilter(self)
        # 最小化、最大化、关闭按钮事件
        self.minButton.clicked.connect(self.showMinimized)
        self.maxButton.clicked.connect(self.toggle_max)
        self.closeButton.clicked.connect(self.close)

    def addLeftWidget(self, widget: QWidget):
        """在标题栏左侧添加控件"""
        self.ribbonWidget.titleWidget.addLeftWidget(widget)

    def addRightWidget(self, widget: QWidget):
        """在标题栏右侧添加控件"""
        self.ribbonWidget.titleWidget.addRightWidget(widget)

    @property
    def title(self):
        """标题文字"""
        return self.ribbonWidget.titleWidget.title

    @title.setter
    def title(self, title):
        """设置标题文字"""
        self.ribbonWidget.titleWidget.title = title

    @property
    def minButton(self):
        """最小化按钮"""
        return self.ribbonWidget.titleWidget.minButton

    @property
    def maxButton(self):
        """最大化按钮"""
        return self.ribbonWidget.titleWidget.maxButton

    @property
    def closeButton(self):
        """关闭按钮"""
        return self.ribbonWidget.titleWidget.closeButton

    @property
    def fileButton(self):
        """文件按钮"""
        return self.ribbonWidget.groupPanel.fileButton

    def addGroup(self, name: str, widget: QWidget):
        """
        添加分组
        :param name: 分组名称
        :param widget: 分组控件
        :return:
        """
        widget.setMouseTracking(True)
        self.ribbonWidget.groupPanel.addTab(widget, name)

    def currentIndex(self):
        """当前组索引"""
        return self.ribbonWidget.groupPanel.currentIndex()

    def removeGroup(self, index):
        """根据索引删除组"""
        self.ribbonWidget.groupPanel.removeTab(index)

    def mouseDoubleClickEvent(self, event):
        """双击全屏"""
        super(QRibbonWindow, self).mouseDoubleClickEvent(event)
        self.toggle_max()

    def toggle_max(self):
        """切换最大化"""
        if self.maxButton.text() == '🗖':
            self.maxButton.setText('🗗')
            self.showMaximized()
        else:
            self.maxButton.setText('🗖')
            self.showNormal()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    # 初始化主窗口
    form = QRibbonWindow()
    form.title = '这是一个标题'
    form.addGroup('开始', QLabel('sss'))
    form.addGroup('设计', QLabel('ddd'))
    form.resize(800, 600)
    form.show()

    from pyqss import Qss

    qss = Qss(form)
    qss.show()

    app.exec_()
