# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 10:20
# @Author  : llc
# @File    : framelessWindow.py

from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtGui import QEnterEvent, QPainter, QPen, QColor, QLinearGradient
from PyQt5.QtWidgets import QMainWindow


class FramelessWindow(QMainWindow):
    resized = pyqtSignal()
    margin = 6
    default = ""

    def __init__(self, parent=None):
        super(FramelessWindow, self).__init__(parent)
        self.top_drag = False
        self.bottom_drag = False
        self.left_drag = False
        self.right_drag = False
        self.bottom_left_drag = False
        self.bottom_right_drag = False
        self.top_left_drag = False
        self.top_right_drag = False
        self.start_mouse_pos = None  # 鼠标按压时鼠标位置
        self.start_window_pos = None  # 鼠标按压时窗口位置
        self.start_width = None  # 鼠标按压时窗口宽度
        self.start_height = None  # 鼠标按压时窗口高度
        self.move_flag = False
        self._rect = []
        self.top_rect = []
        self.bottom_rect = []
        self.left_rect = []
        self.right_rect = []
        self.bottom_left_rect = []
        self.bottom_right_rect = []
        self.top_left_rect = []
        self.top_right_rect = []
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Dialog |
                            Qt.FramelessWindowHint |
                            Qt.WindowSystemMenuHint |
                            Qt.WindowMinMaxButtonsHint)
        self.calc_rect()

    def mousePressEvent(self, event):
        if self.isMaximized():
            return
        self.start_mouse_pos = event.globalPos()
        self.start_window_pos = self.pos()
        self.start_width = self.width()
        self.start_height = self.height()
        if (event.button() == Qt.LeftButton) and (event.pos() in self.top_rect):
            # 上
            self.top_drag = True
        elif (event.button() == Qt.LeftButton) and (event.pos() in self.bottom_rect):
            # 下
            self.bottom_drag = True
        elif (event.button() == Qt.LeftButton) and (event.pos() in self.left_rect):
            # 左
            self.left_drag = True
        elif (event.button() == Qt.LeftButton) and (event.pos() in self.right_rect):
            # 右
            self.right_drag = True
        elif (event.button() == Qt.LeftButton) and (event.pos() in self.bottom_left_rect):
            # 左下
            self.bottom_left_drag = True
        elif (event.button() == Qt.LeftButton) and (event.pos() in self.bottom_right_rect):
            # 右下
            self.bottom_right_drag = True
        elif (event.button() == Qt.LeftButton) and (event.pos() in self.top_left_rect):
            # 左上
            self.top_left_drag = True
        elif (event.button() == Qt.LeftButton) and (event.pos() in self.top_right_rect):
            # 右上
            self.top_right_drag = True
        elif event.button() == Qt.LeftButton:
            # 移动
            self.move_flag = True
        event.accept()

    def mouseMoveEvent(self, event):
        if self.isMaximized():
            return
        # print(event.pos())
        if event.pos() in self.top_rect:
            # 上
            self.setCursor(Qt.SizeVerCursor)
        elif event.pos() in self.bottom_rect:
            # 下
            self.setCursor(Qt.SizeVerCursor)
        elif event.pos() in self.left_rect:
            # 左
            self.setCursor(Qt.SizeHorCursor)
        elif event.pos() in self.right_rect:
            # 右
            self.setCursor(Qt.SizeHorCursor)
        elif event.pos() in self.bottom_left_rect:
            # 左下
            self.setCursor(Qt.SizeBDiagCursor)
        elif event.pos() in self.bottom_right_rect:
            # 右下
            self.setCursor(Qt.SizeFDiagCursor)
        elif event.pos() in self.top_left_rect:
            # 左上
            self.setCursor(Qt.SizeFDiagCursor)
        elif event.pos() in self.top_right_rect:
            # 右上
            self.setCursor(Qt.SizeBDiagCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

        if not self.start_mouse_pos:
            return

        diff_x = event.globalPos().x() - self.start_mouse_pos.x()
        diff_y = event.globalPos().y() - self.start_mouse_pos.y()
        if diff_x > 0 and self.width() == self.minimumWidth():
            return
        if diff_y < 0 and self.height() == self.minimumHeight():
            return

        elif Qt.LeftButton and self.top_drag:
            # 上
            diff_y = event.globalPos().y() - self.start_mouse_pos.y()
            if diff_y > 0 and self.height() == self.minimumHeight():
                return
            self.setGeometry(self.pos().x(), self.start_window_pos.y() + diff_y, self.width(),
                             self.start_height - diff_y)
            event.accept()
        elif Qt.LeftButton and self.bottom_drag:
            # 下
            self.resize(self.width(), event.pos().y())
            event.accept()
        elif Qt.LeftButton and self.left_drag:
            # 左
            diff_x = event.globalPos().x() - self.start_mouse_pos.x()
            if diff_x > 0 and self.width() == self.minimumWidth():
                return
            self.setGeometry(self.start_window_pos.x() + diff_x, self.pos().y(), self.start_width - diff_x,
                             self.height())
            event.accept()
        elif Qt.LeftButton and self.right_drag:
            # 右
            self.resize(event.pos().x(), self.height())
            event.accept()
        elif Qt.LeftButton and self.bottom_left_drag:
            # 左下
            self.setGeometry(self.start_window_pos.x() + diff_x, self.pos().y(), self.start_width - diff_x,
                             self.start_height + diff_y)
            event.accept()
        elif Qt.LeftButton and self.bottom_right_drag:
            # 右下
            self.resize(event.pos().x(), event.pos().y())
            event.accept()
        elif Qt.LeftButton and self.top_left_drag:
            # 左上
            self.setGeometry(self.start_window_pos.x() + diff_x, self.start_window_pos.y() + diff_y,
                             self.start_width - diff_x,
                             self.start_height - diff_y)
            event.accept()
        elif Qt.LeftButton and self.top_right_drag:
            # 右上
            self.setGeometry(self.pos().x(), self.start_window_pos.y() + diff_y, self.start_width + diff_x,
                             self.start_height - diff_y)
            event.accept()
        elif event.buttons() == Qt.LeftButton and self.start_mouse_pos and self.move_flag:
            # 移动
            diff_x = event.globalPos() - self.start_mouse_pos
            self.move(self.start_window_pos + diff_x)
            self.calc_rect()
            event.accept()

    def mouseReleaseEvent(self, event):
        if self.isMaximized():
            return
        x, y, width, height = self.geometry().getRect()
        if y < 0:
            self.setGeometry(x, 1, width, height)
        self.top_drag = False
        self.bottom_drag = False
        self.left_drag = False
        self.right_drag = False
        self.bottom_left_drag = False
        self.bottom_right_drag = False
        self.top_left_drag = False
        self.top_right_drag = False
        self.start_mouse_pos = None
        event.accept()

    def calc_rect(self):
        width, height = self.width(), self.height()
        margin = self.margin
        self.top_rect = [QPoint(x, y) for x in range(margin, width - margin) for y in range(0, margin)]
        self.bottom_rect = [QPoint(x, y) for x in range(margin, width - margin) for y in range(height - margin, height)]
        self.left_rect = [QPoint(x, y) for x in range(0, margin) for y in range(margin, height - margin)]
        self.right_rect = [QPoint(x, y) for x in range(width - margin, width) for y in range(margin, height - margin)]
        self.bottom_left_rect = [QPoint(x, y) for x in range(0, margin) for y in range(height - margin, height)]
        self.bottom_right_rect = [QPoint(x, y) for x in range(width - margin, width) for y in
                                  range(height - margin, height)]
        self.top_left_rect = [QPoint(x, y) for x in range(0, margin) for y in range(0, margin)]
        self.top_right_rect = [QPoint(x, y) for x in range(width - margin, width) for y in range(0, margin)]

    def resizeEvent(self, event) -> None:
        super(FramelessWindow, self).resizeEvent(event)
        self.calc_rect()
        if self.isMaximized():
            self.setStyleSheet(self.default.replace("{{margin}}", "0"))
        else:
            self.setStyleSheet(self.default.replace("{{margin}}", str(self.margin)))
        self.resized.emit()

    def eventFilter(self, obj, event):
        """事件过滤器,用于解决鼠标进入其它控件后还原为标准鼠标样式"""

        if isinstance(event, QEnterEvent):
            self.setCursor(Qt.ArrowCursor)
            obj.setCursor(Qt.ArrowCursor)

        return super(FramelessWindow, self).eventFilter(obj, event)

    def paintEvent(self, event):
        super(FramelessWindow, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        color1 = QColor(255, 255, 255, 2)
        color2 = QColor(0, 0, 0, 4)
        if not self.isMaximized():
            # 上
            painter.save()
            linearGradient = QLinearGradient(0, 0, 0, self.margin)
            linearGradient.setColorAt(0, color1)
            linearGradient.setColorAt(1, color2)
            painter.setBrush(linearGradient)
            painter.setPen(Qt.transparent)
            painter.drawRect(0, 0, self.width() - self.margin, self.margin)
            painter.restore()
            # 下
            painter.save()
            linearGradient = QLinearGradient(0, self.height() - self.margin, 0, self.height())
            linearGradient.setColorAt(0, color2)
            linearGradient.setColorAt(1, color1)
            painter.setBrush(linearGradient)
            painter.setPen(Qt.transparent)
            painter.drawRect(0, self.height() - self.margin, self.width(), self.height())
            painter.restore()
            # 左
            painter.save()
            linearGradient = QLinearGradient(0, 0, self.margin, 0)
            linearGradient.setColorAt(0, color1)
            linearGradient.setColorAt(1, color2)
            painter.setBrush(linearGradient)
            painter.setPen(Qt.transparent)
            painter.drawRect(0, 0, self.margin, self.height())
            painter.restore()
            # 右
            painter.save()
            linearGradient = QLinearGradient(self.width() - self.margin, 0, self.width(), 0)
            linearGradient.setColorAt(0, color2)
            linearGradient.setColorAt(1, color1)
            painter.setBrush(linearGradient)
            painter.setPen(Qt.transparent)
            painter.drawRect(self.width() - self.margin, 0, self.width(), self.height())
            painter.restore()
        # 绘制1像素黑边
        painter.save()
        painter.setPen(QPen(QColor(131, 131, 131), 1))
        painter.drawRect(self.margin, self.margin, self.width() - 2 * self.margin,
                         self.height() - 2 * self.margin)
        painter.restore()
