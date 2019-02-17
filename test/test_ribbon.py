# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 9:06
# @Author  : llc
# @File    : test_ribbon.py
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QGridLayout, QStatusBar, QDockWidget, QCalendarWidget, QWidget, QLabel
from PyQRibbon import QRibbonWidget, QRibbonWindow


class Form(QRibbonWindow):
    # 继承QRibbonWindow
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.resize(800, 600)
        self.init_ui()

    def init_ui(self):
        ribbon_widget = QRibbonWidget(self)
        # 标题栏
        title_bar = ribbon_widget.title_bar
        title_bar.set_title('这是一个标题')
        title_bar.add_widget('image/left.ico', left=True)
        title_bar.add_widget('image/right.ico', left=False)
        # 菜单栏
        tabmenu_bar = ribbon_widget.tabmenu_bar
        menu = tabmenu_bar.add_menu('开始')
        # 工具组
        group = tabmenu_bar.add_group('剪切板', menu)
        # 工具组右下角按钮
        corner = group.corner
        corner.clicked.connect(lambda: print('test'))
        # 添加widget
        label = QLabel()
        label.setPixmap(QPixmap('image/cut.png'))
        group.add_widget(label)
        # -------------------------------------------
        group = tabmenu_bar.add_group('字体', menu)
        label = QLabel()
        label.setPixmap(QPixmap('image/font.png'))
        group.add_widget(label)
        menu = tabmenu_bar.add_menu('插入')
        group = tabmenu_bar.add_group('剪切板11', menu)
        group = tabmenu_bar.add_group('字体11', menu)
        menu = tabmenu_bar.add_menu('设计')
        menu = tabmenu_bar.add_menu('布局管理')

        self.setWindowIcon(QIcon('image/left.ico'))
        self.addToolBar(ribbon_widget)

        self.centralwidget = QWidget(self)
        gridLayout = QGridLayout(self.centralwidget)
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


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
