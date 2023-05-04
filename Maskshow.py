# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.Qt import QPixmap, QPoint, Qt, QPainter
import sys
from PyQt5.QtGui import *

class ImageBox(QWidget):
    def __init__(self):
        super().__init__()
        self.img = None
        self.scaled_img = None
        self.point = QPoint(0, 0)
        self.start_pos = None
        self.end_pos = None
        self.left_click = False
        self.scale = 0.5

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ImageBox")

    def set_image(self, mask_path):
        self.img = QPixmap(mask_path)
        self.scaled_img = self.img.scaled(self.size())

    def paintEvent(self, e):
        if self.scaled_img:
            painter = QPainter(self)
            painter.scale(self.scale, self.scale)
            painter.drawPixmap(self.point, self.scaled_img)

    def mouseMoveEvent(self, e):
        if self.left_click:
            if self.start_pos is None:
                self.start_pos = e.pos()
            else:
                self.end_pos = e.pos() - self.start_pos
                self.point += self.end_pos
                self.start_pos = e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self.start_pos = e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = False
            self.start_pos = None
            self.end_pos = None


#the app window for show picture and adjust
class MainDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Result Show")
        self.setFixedSize(600, 600)

        # zoom in and out buttons
        self.zoom_in = QPushButton("+")
        self.zoom_in.clicked.connect(self.large_click)
        self.zoom_in.setFixedSize(30, 30)

        self.zoom_out = QPushButton("-")
        self.zoom_out.clicked.connect(self.small_click)
        self.zoom_out.setFixedSize(30, 30)

        # layout for buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.zoom_in)
        buttons_layout.addWidget(self.zoom_out)
        buttons_layout.setAlignment(Qt.AlignLeft)

        # widget for buttons layout
        buttons_widget = QWidget(self)
        buttons_widget.setLayout(buttons_layout)
        buttons_widget.setFixedSize(550, 50)

        self.box = ImageBox()
        self.box.resize(512, 512)

        mask_path = './images/result.jpg'
        self.box.set_image(mask_path)
        self.update()

        # layout for entire widget
        main_layout = QVBoxLayout()
        main_layout.addWidget(buttons_widget)
        main_layout.addWidget(self.box)
        self.setLayout(main_layout)

    # open image from result path
    def open_image(self):
        mask_path = './images/result.jpg'
        self.box.set_image(mask_path)
        self.update()

    # zoom in function
    def large_click(self):
        if self.box.scale < 2:
            self.box.scale += 0.1
            self.box.adjustSize()
            self.update()

    # zoom out function
    def small_click(self):
        if self.box.scale > 0.1:
            self.box.scale -= 0.2
            self.box.adjustSize()
            self.update()
