# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/4/10 16:39
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QToolButton, QPushButton, QAction, QSizePolicy, QLabel, \
    QMenu, QHBoxLayout, QTextEdit

from PyQRibbon import QRibbonWindow


class Notepad(QRibbonWindow):
    def __init__(self):
        super(Notepad, self).__init__()
        self.resize(800, 600)

        # 设置标题
        self.title = "记事本"

        # 左侧添加按钮
        saveBtn = QPushButton(QIcon('images/save.png'), '')
        self.addLeftWidget(saveBtn)
        saveBtn.setMouseTracking(True)

        # 右侧添加按钮
        self.addRightWidget(QPushButton(QIcon("./images/smile.png"), ''))

        # 文件按钮点击事件
        fileButton = self.addFileButton("文件")
        fileButton.clicked.connect(lambda: print('file clicked'))

        # 添加标签
        tab = self.addTab("开始")
        widget = QWidget(tab)
        widget.setObjectName("groupWidget")
        gridLayout = QGridLayout(widget)
        gridLayout.setContentsMargins(3, 3, 3, 3)
        gridLayout.setSpacing(0)
        pasteToolBtn = QToolButton(widget)
        pasteToolBtn.setObjectName("pasteToolBtn")
        pasteToolBtn.setAutoRaise(True)
        pasteToolBtn.clicked.connect(lambda: print("clicked"))
        pasteToolBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        pasteToolBtn.setPopupMode(QToolButton.MenuButtonPopup)
        pasteToolBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 设置菜单
        menu = QMenu(pasteToolBtn)
        menu.addAction(QAction("粘贴", menu))
        menu.addAction(QAction("粘贴为纯文本", menu))
        pasteToolBtn.setMenu(menu)
        pasteToolBtn.setIcon(QIcon('./images/paste.png'))
        pasteToolBtn.setText('粘贴')
        pasteToolBtn.setDefaultAction(QAction(QIcon("./images/paste.png"), "test"))

        gridLayout.addWidget(pasteToolBtn, 0, 0, 3, 1)
        cutBtn = QPushButton(QIcon("./images/cut.png"), "剪切", widget)
        cutBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        gridLayout.addWidget(cutBtn, 0, 1, 1, 1)
        copyBtn = QPushButton(QIcon("./images/copy.png"), "复制", widget)
        copyBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        gridLayout.addWidget(copyBtn, 1, 1, 1, 1)
        brushBtn = QPushButton(QIcon("./images/format.png"), "格式刷", widget)
        brushBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        gridLayout.addWidget(brushBtn, 2, 1, 1, 1)
        # 添加分组
        tab.addGroup("剪贴板", widget, corner=True, cornerCallback=lambda: print('clicked'))
        # 添加分组
        widget = QLabel('在这里添加一个控件...')
        tab.addGroup("文件", widget)

        # 添加第二个标签
        tab = self.addTab('插入')
        tab.addGroup('设计', QLabel("在这里添加一个控件..."))

        # 添加写字板
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit = QTextEdit(self.centralWidget)
        self.textEdit.setMouseTracking(True)
        self.textEdit.setHtml("""
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; color:#00aaff;">PyQRibbon</span>是一个实现了<span style=" font-size:12pt; color:#ff007f;">ribbon</span>菜单的控件</p></body></html>""")
        self.horizontalLayout.addWidget(self.textEdit)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    form = Notepad()
    form.show()

    # 设置样式
    app.setStyleSheet(open('./notepad.qss').read())

    # from pyqss import Qss
    #
    # qss = Qss(form)
    # qss.show()

    app.exec_()
