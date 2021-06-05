# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/5/3 13:24
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QToolBar

from PyQRibbon.theme import default
from PyQRibbon.widgets.framelessWindow import FramelessWindow
from PyQRibbon.widgets.ribbonWidget import QRibbonWidget, QLabel, QTab


class QRibbonWindow(FramelessWindow):
    def __init__(self, style='default'):
        super(QRibbonWindow, self).__init__()
        self.style = style
        self.setObjectName('QRibbonWindow')

        self.tabs = []
        self.groups = []

        # 设置样式
        self.default = default
        if self.style == 'default':
            _default = default.replace("{{margin}}", str(self.margin))
            self.setStyleSheet(_default + '\n' + self.styleSheet())
        # 去除右键菜单
        self.setContextMenuPolicy(Qt.NoContextMenu)
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
        self.ribbonWidget.tabPanel.installEventFilter(self)
        self.minButton.installEventFilter(self)
        self.maxButton.installEventFilter(self)
        self.closeButton.installEventFilter(self)
        # 最小化、最大化、关闭按钮事件
        self.minButton.clicked.connect(self.showMinimized)
        self.maxButton.clicked.connect(self.toggle_max)
        self.closeButton.clicked.connect(self.close)

    def addLeftWidget(self, widget: QWidget):
        """在标题栏左侧添加控件"""
        widget.setMouseTracking(True)
        self.ribbonWidget.titleWidget.addLeftWidget(widget)

    def addRightWidget(self, widget: QWidget):
        """在标题栏右侧添加控件"""
        widget.setMouseTracking(True)
        self.ribbonWidget.titleWidget.addRightWidget(widget)

    def addFileButton(self, text='文件'):
        fileButton = self.ribbonWidget.tabPanel.addFileButton(text)
        fileButton.setMouseTracking(True)
        fileButton.installEventFilter(self)

        return fileButton

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
        return self.ribbonWidget.tabPanel.fileButton

    def addTab(self, name: str):
        """添加tab"""
        tab = QTab(self.ribbonWidget.tabPanel)
        self.ribbonWidget.tabPanel.addTab(tab, name)
        self.tabs.append(tab)
        return tab

    def currentIndex(self):
        """当前tab索引"""
        return self.ribbonWidget.tabPanel.currentIndex()

    def mouseDoubleClickEvent(self, event):
        """双击全屏"""
        super(QRibbonWindow, self).mouseDoubleClickEvent(event)
        # 左键
        if event.buttons() == Qt.LeftButton:
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
    tab1 = form.addTab('开始')
    tab1.addGroup('剪贴板', QLabel('ttt'), corner=True, cornerCallback=lambda: print(111))
    tab1.addGroup("字体", QLabel('ddd'))
    tab2 = form.addTab('设计')
    tab2.addGroup("格式", QLabel('sss'))
    form.resize(800, 600)
    form.show()

    from pyqss import Qss

    qss = Qss(form)
    qss.show()

    app.exec_()
