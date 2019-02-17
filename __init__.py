# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 13:22
# @Author  : llc
# @File    : __init__.py

from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QToolBar, QMainWindow
from .widgets import _QRibbonWidget
from . import icons_rc
import os


class QRibbonWidget(QToolBar):
    def __init__(self, parent=None):
        super(QRibbonWidget, self).__init__(parent)
        self._ribbonwindow = parent
        self.setStyleSheet(open(os.path.join(os.path.dirname(__file__), 'qss/QRibbonWidget.qss')).read())
        self._init()
        self.setMouseTracking(True)

    def _init(self):
        if not isinstance(self._ribbonwindow, QRibbonWindow):
            raise TypeError("__init__(self, parent=None) 'parent' requires 'QRibbonWindow' type.")

        self._ribbon_widget = _QRibbonWidget(self._ribbonwindow)
        self.addWidget(self._ribbon_widget)
        self.setAllowedAreas(Qt.NoToolBarArea)
        self.setMovable(False)
        self.setFloatable(False)
        self._ribbonwindow.addToolBar(self)

    @property
    def title_bar(self):
        return self._ribbon_widget.title_bar

    @property
    def tabmenu_bar(self):
        return self._ribbon_widget.menu_bar


class QRibbonWindow(QMainWindow):
    double_click = pyqtSignal()

    def __init__(self, *args):
        super(QRibbonWindow, self).__init__(*args)
        self._bottom_drag = False
        self._left_drag = False
        self._right_drag = False
        self._bottom_right_drag = False
        self._bottom_left_drag = False
        self._start_point = None
        self.setMouseTracking(True)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setWindowFlags(Qt.Window |
                            Qt.FramelessWindowHint |
                            Qt.WindowSystemMenuHint |
                            Qt.WindowMinMaxButtonsHint |
                            Qt.WindowCloseButtonHint)

    def mousePressEvent(self, event):
        self._start_point = event.globalPos()
        self._pos = self.pos()
        self._width = self.width()
        self._height = self.height()

        if (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_rect):
            # 下
            self._bottom_drag = True
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._left_rect):
            # 左
            self._left_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._right_rect):
            # 右
            self._right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_right_corner_rect):
            # 右下
            self._bottom_right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_left_corner_rect):
            # 左下
            self._bottom_left_drag = True
            event.accept()
        elif event.button() == Qt.LeftButton:
            # 移动
            event.accept()

    def mouseMoveEvent(self, event):
        if event.pos() in self._bottom_rect:
            # 下
            self.setCursor(Qt.SizeVerCursor)
        elif event.pos() in self._left_rect:
            # 左
            self.setCursor(Qt.SizeHorCursor)
        elif event.pos() in self._right_rect:
            # 右
            self.setCursor(Qt.SizeHorCursor)
        elif event.pos() in self._bottom_right_corner_rect:
            # 右下
            self.setCursor(Qt.SizeFDiagCursor)
        elif event.pos() in self._bottom_left_corner_rect:
            # 左下
            self.setCursor(Qt.SizeBDiagCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

        if self.isMaximized():
            # 最大化时什么也不做
            return

        if not self._start_point:
            return
        elif Qt.LeftButton and self._bottom_drag:
            # 下
            self.resize(self.width(), event.pos().y())
            event.accept()
        elif Qt.LeftButton and self._left_drag:
            # 左
            diff_x = event.globalPos().x() - self._start_point.x()
            if diff_x > 0 and self.width() == self.minimumWidth():
                return
            self.setGeometry(self._pos.x() + diff_x, self.pos().y(), self._width - diff_x, self.height())
            event.accept()
        elif Qt.LeftButton and self._right_drag:
            # 右
            self.resize(event.pos().x(), self.height())
            event.accept()
        elif Qt.LeftButton and self._bottom_right_drag:
            # 右下
            self.resize(event.pos().x(), event.pos().y())
            event.accept()
        elif Qt.LeftButton and self._bottom_left_drag:
            # 左下
            diff_x = event.globalPos().x() - self._start_point.x()
            diff_y = event.globalPos().y() - self._start_point.y()
            if diff_x > 0 and self.width() == self.minimumWidth():
                return
            if diff_y < 0 and self.height() == self.minimumHeight():
                return
            self.setGeometry(self._pos.x() + diff_x, self.pos().y(), self._width - diff_x, self._height + diff_y)
            event.accept()
        elif event.buttons() == Qt.LeftButton and self._start_point:
            diff_x = event.globalPos() - self._start_point
            self.move(self._pos + diff_x)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._bottom_drag = False
        self._left_drag = False
        self._right_drag = False
        self._bottom_right_drag = False
        self._bottom_left_drag = False
        self._start_point = None
        event.accept()

    def mouseDoubleClickEvent(self, event):
        self.double_click.emit()

    def resizeEvent(self, event):
        self._bottom_rect = [QPoint(x, y) for x in range(10, self.width() - 10) for y in
                             range(self.height() - 10, self.height() + 10)]
        self._left_rect = [QPoint(x, y) for x in range(-10, 10) for
                           y in range(10, self.height() - 10)]
        self._right_rect = [QPoint(x, y) for x in range(self.width() - 10, self.width() + 10) for
                            y in range(10, self.height() - 10)]
        self._bottom_right_corner_rect = [QPoint(x, y) for x in range(self.width() - 10, self.width() + 10) for
                                          y in range(self.height() - 10, self.height() + 10)]
        self._bottom_left_corner_rect = [QPoint(x, y) for x in range(-10, 10) for
                                         y in range(self.height() - 10, self.height() + 10)]
