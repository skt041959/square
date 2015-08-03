#!/usr/bin/env python
# encoding: utf-8

from PyQt4.QtGui import QPushButton
from PyQt4.QtCore import QSize

class Piece(QPushButton):

    def __init__(self, parent, color, shape):
        super(Piece, self).__init__(parent)
        self.color = color
        self.shape = shape

        self.setFixedSize(QSize(100, 100))

