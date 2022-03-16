# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/4/10 16:36
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QSizePolicy, QTabWidget, QFrame, QSpacerItem

from PyQRibbon.theme import foldIcon, fixedIcon
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


class QTabPanel(QTabWidget):
    def __init__(self, parent=None):
        super(QTabPanel, self).__init__(parent)
        self.isFold = False

        self.setMouseTracking(True)

        self.currentChanged.connect(self.updateStyleSheet)
        # 折叠按钮
        self.foldButton = QPushButton(QIcon(foldIcon), '')
        self.foldButton.setStyleSheet("""
                border:0px;
                width:25px;
                height:15px;
            """)
        self.foldButton.clicked.connect(self.foldButtonClicked)
        self.setCornerWidget(self.foldButton, corner=Qt.TopRightCorner)
        # tab单击事件
        self.tabBarClicked.connect(self.tabBarUpdate)

    def addFileButton(self, text):
        fileButton = QFileButton(text, self)
        self.setCornerWidget(fileButton, corner=Qt.TopLeftCorner)

        return fileButton

    def updateStyleSheet(self):
        self.setStyleSheet("")
        self.isFold = False
        self.foldButton.setIcon(QIcon(foldIcon))

    def foldButtonClicked(self):
        if not self.isFold:
            self.foldButton.setIcon(QIcon(fixedIcon))
            self.setStyleSheet("""
                    QTabPanel {
                        min-height: 30px;
                        max-height: 30px;
                    }
                    QTabPanel  QTabBar::tab:selected{
                        border-left: 0px;
                        border-top: 0px;
                        border-right: 0px;
                        color: rgb(43, 87, 154);
                    }
                    QTabPanel:pane{
                        top: 0px;
                        border-top: 0px;
                        border-bottom: 0px;
                        background-color: rgb(255, 255, 255);
                    }
                    """)
        else:
            self.foldButton.setIcon(QIcon(foldIcon))
            self.setStyleSheet("")
        self.isFold = not self.isFold

    def tabBarUpdate(self, index):
        if index == self.currentIndex():
            self.setStyleSheet("")
            self.isFold = False
            self.foldButton.setIcon(QIcon(foldIcon))


class QTab(QBaseWidget):
    def __init__(self, parent=None):
        super(QTab, self).__init__(parent)

        self.__init_ui()

    def __init_ui(self):
        """水平布局，用于添加group"""
        self.__layout = create_layout(self)
        # 最右侧添加弹簧
        horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.__layout.addItem(horizontalSpacer)

    def addGroup(self, name, widget, corner=False, cornerCallback=None):
        group = QGroup(name, widget, corner, cornerCallback, self)
        # 控件个数
        count = self.__layout.count()
        self.__layout.insertWidget(count - 1, group)
        # 添加竖线
        line = QFrame(self)
        line.setObjectName("Line")
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Raised)
        self.__layout.insertWidget(count, line)
        return group


class QGroup(QBaseWidget):
    def __init__(self, name, widget, corner=False, cornerCallback=None, parent=None):
        """
        组控件
        :param name: 名称
        :param widget: 控件
        :param corner: 右下角按钮是否实现显示
        :param cornerCallback: 右下角按钮点击回调函数
        :param parent: 父级
        """
        super(QGroup, self).__init__(parent)
        self.name = name
        self.widget = widget
        self.corner = corner
        self.cornerCallback = cornerCallback
        self.__init_ui()

        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)

    def __init_ui(self):
        """网格布局"""
        vl = create_layout(self, 'v')
        self.widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        vl.addWidget(self.widget)
        hl = create_layout(direction='h')
        horizontalSpacerL = QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hl.addItem(horizontalSpacerL)
        label = QLabel(self.name, self)
        label.setObjectName("GroupLabel")
        hl.addWidget(label)
        horizontalSpacerR = QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hl.addItem(horizontalSpacerR)
        cornerButton = QPushButton('⟓', self)
        cornerButton.setObjectName('cornerButton')
        cornerButton.hide()
        hl.addWidget(cornerButton)
        vl.addLayout(hl)
        if self.corner:
            cornerButton.show()
            if self.cornerCallback:
                cornerButton.clicked.connect(self.cornerCallback)


class QRibbonWidget(QFrame):
    def __init__(self, parent=None):
        super(QRibbonWidget, self).__init__(parent)
        # 标题组件
        self.titleWidget = QTitleWidget(self)
        # 分组组件
        self.tabPanel = QTabPanel(self)
        # 创建垂直布局
        vl = create_layout(self, direction='v')
        vl.addWidget(self.titleWidget)
        vl.addWidget(self.tabPanel)

        self.setMouseTracking(True)
