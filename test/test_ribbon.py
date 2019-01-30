# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 9:06
# @Author  : llc
# @File    : test_ribbon.py
from PyQt5.QtGui import QIcon
from PyQRibbon import QRibbonWidget, QRibbonWindow


class Form(QRibbonWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.resize(800, 600)
        ribbon_widget = QRibbonWidget(self)
        self.addToolBar(ribbon_widget)

        ribbon_widget.title_bar.set_title('这是一个标题')
        ribbon_widget.title_bar.add_widget('image/left.ico', left=True)
        ribbon_widget.title_bar.add_widget('image/right.ico', left=False)

        ribbon_widget.tabmenu_bar.add_tab('文件')
        ribbon_widget.tabmenu_bar.add_tab('开始')
        ribbon_widget.tabmenu_bar.add_tab('插入')
        ribbon_widget.tabmenu_bar.add_tab('设计')
        ribbon_widget.tabmenu_bar.add_tab('布局')

        self.setWindowIcon(QIcon('image/left.ico'))


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
