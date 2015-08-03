#!/usr/bin/env python
# encoding: utf-8

from PyQt4.QtGui import QPushButton,QPainter,QImage,QIcon,QPixmap,QColor
from PyQt4.QtCore import QSize,QRect
from PyQt4.QtCore import Qt

class Piece(QPushButton):

    cellCoor = [[(0, 2)],
            [(0, 2), (1, 2)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 2), (1, 2), (2, 2), (3, 2)],
            [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2)],
            ]

    colors = {"red":Qt.red, "blue":Qt.blue, "green":Qt.green, "yellow":Qt.yellow}

    def __init__(self, parent, color, shape):
        super(Piece, self).__init__(parent)

        self.color = color
        self.shape = shape
        cells = [QRect(11*x+1, 11*y+1, 10, 10) for x,y in self.cellCoor[self.shape]]

        self.setFixedSize(QSize(100, 100))

        self.setCheckable(True)

        self.i = QImage(56, 56, QImage.Format_ARGB32)
        self.i.fill(0x000000FF)

        p = QPainter(self.i)
        p.setBrush(self.colors[self.color])
        p.drawRects(cells)

        self.setIconSize(QSize(56, 56))
        self.setIcon(QIcon(QPixmap.fromImage(self.i)))



