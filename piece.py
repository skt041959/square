#!/usr/bin/env python
# encoding: utf-8

from PyQt4.QtGui import QPushButton,QPainter,QImage,QIcon,QPixmap,QColor
from PyQt4.QtCore import QSize,QRect
from PyQt4.QtCore import Qt

class Piece(QPushButton):

    cellCoor = [[(2, 2)],
            [(1, 2), (2, 2)],
            [(1, 2), (2, 2), (3, 2)],
            [(1, 2), (2, 2), (2, 1)],
            [(1, 1), (1, 2), (2, 1), (2, 2)],
            [(0, 2), (1, 2), (2, 2), (2, 1)],
            [(0, 2), (1, 2), (2, 2), (3, 2)],
            [(1, 2), (2, 2), (2, 1), (3, 1)],
            [(1, 2), (2, 2), (2, 1), (3, 2)],
            [(0, 2), (1, 2), (2, 2), (3, 2), (3, 1)],
            [(1, 1), (1, 2), (2, 1), (2, 2), (3, 2)],
            [(1, 1), (2, 1), (2, 2), (3, 2), (3, 3)],
            [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)],
            [(1, 1), (1, 2), (2, 2), (3, 2), (3, 3)],
            [(2, 1), (1, 2), (2, 2), (3, 2), (3, 3)],
            [(0, 2), (1, 2), (2, 2), (2, 1), (3, 1)],
            [(1, 1), (1, 2), (2, 2), (3, 2), (3, 1)],
            [(0, 2), (1, 2), (2, 2), (2, 1), (3, 2)],
            [(2, 1), (1, 2), (2, 2), (3, 2), (2, 3)],
            [(1, 1), (1, 2), (2, 2), (3, 2), (1, 3)],
            [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
            ]

    colors = {"red":Qt.red, "blue":Qt.blue, "green":Qt.green, "yellow":Qt.yellow}

    def __init__(self, parent, color, shape):
        super(Piece, self).__init__(parent)

        self.color = color
        self.shape = shape
        cells = [QRect(11*x, 11*y, 11, 11) for x,y in self.cellCoor[self.shape]]

        self.setFixedSize(QSize(100, 100))

        self.setCheckable(True)

        self.i = QImage(56, 56, QImage.Format_ARGB32)
        self.i.fill(0x000000FF)

        p = QPainter(self.i)
        p.setBrush(self.colors[self.color])
        p.setPen(QColor(255, 255, 255, 255))
        p.drawRects(cells)

        self.setIconSize(QSize(56, 56))
        self.setIcon(QIcon(QPixmap.fromImage(self.i)))

        self.fliped = False
        self.rotated = 0

        self.d = QImage(256, 256, QImage.Format_ARGB32)
        self.updateImage()

    def rotate(self, action):
        if action > 0:
            self.rotated += 1
        else:
            self.rotated -= 1

        self.rotated = self.rotated % 4
        self.updateImage()

    def flip(self):
        self.fliped = not self.fliped
        self.updateImage()

    def updateImage(self):
        c = self.cellCoor[self.shape]

        if self.fliped > 0:
            c = [(4-x, y) for x,y in c]

        action = self.rotated

        while action > 0:
            c = [(y, 4-x) for x,y in c]
            action -= 1

        cells = [QRect(51*x, 51*y, 51, 51) for x,y in c]

        self.d.fill(0x000000FF)

        p = QPainter(self.d)
        p.setBrush(self.colors[self.color])
        p.setPen(QColor(255, 255, 255, 255))
        p.drawRects(cells)

    def getImage(self):
        return self.d



