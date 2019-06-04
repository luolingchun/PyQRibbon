# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 9:06
# @Author  : llc
# @File    : test_ribbon.py
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QGridLayout, QStatusBar, QDockWidget, QCalendarWidget, QWidget, QLabel
from PyQRibbon import QRibbonToolBar
from PyQRibbon.widgets.frameless_window import FramelessWindow


class Form(FramelessWindow):
    # 继承QRibbonWindow
    def __init__(self):
        super(Form, self).__init__()
        self.resize(800, 600)
        self.init_ui()

    def init_ui(self):
        ribbon_toolbar = QRibbonToolBar(self)
        # 标题栏
        ribbon_toolbar.title = '这是一个标题'
        ribbon_toolbar.add_widget(icon='image/left.ico', left=True)
        ribbon_toolbar.add_widget(icon='image/right.ico', left=False)
        # 菜单栏
        menu = ribbon_toolbar.add_menu('开始')
        # 工具组
        group = ribbon_toolbar.add_group('剪切板', menu)
        # 工具组右下角按钮
        corner = group.corner
        corner.clicked.connect(lambda: print('test'))
        # 工具组添加widget
        label = QLabel()
        label.setPixmap(QPixmap('image/cut.png'))
        group.add_widget(label)
        group = ribbon_toolbar.add_group('字体', menu)
        label = QLabel()
        label.setPixmap(QPixmap('image/font.png'))
        group.add_widget(label)
        # -------------------------------------------
        menu = ribbon_toolbar.add_menu('插入')
        group = ribbon_toolbar.add_group('剪切板11', menu)
        group = ribbon_toolbar.add_group('字体11', menu)
        menu = ribbon_toolbar.add_menu('设计')
        menu = ribbon_toolbar.add_menu('布局管理')

        self.setWindowIcon(QIcon('image/left.ico'))
        self.addToolBar(ribbon_toolbar)

        self.centralwidget = QWidget(self)
        gridLayout = QGridLayout(self.centralwidget)
        gridLayout.setContentsMargins(self.margin, self.margin, self.margin, self.margin)
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setMouseTracking(True)
        gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setMouseTracking(True)
        dockewidget = QDockWidget(self)
        dockewidget.setMouseTracking(True)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockewidget)
        statusbar = QStatusBar(self)
        statusbar.setMouseTracking(True)
        self.setStatusBar(statusbar)

        ribbon_toolbar.installEventFilter(self)
        self.calendarWidget.installEventFilter(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle('fusion')
    form = Form()
    form.show()
    app.exec_()
