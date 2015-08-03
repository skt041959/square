#!/usr/bin/env python
# encoding: utf-8

from PyQt4.QtGui import QWidget,QPainter,QColor,QImage
from PyQt4.QtCore import QPoint,QSize,QLine,QRect

class Board(QWidget):

    def __init__(self, parent, row, col):
        super(Board,self).__init__(parent)

        self.row = row
        self.col = col

        self.cellwidth = 50
        self.linewidth = 1

        self.width = self.cellwidth*col + self.linewidth*(col+1)
        self.height = self.cellwidth*row + self.linewidth*(row+1)

        self.setFixedSize(self.width, self.height)

        self.board = QImage(self.width, self.height, QImage.Format_ARGB32)

        p = QPainter(self.board)
        p.setBrush(QColor(255, 255, 255, 255))
        p.drawRect(QRect(0, 0, self.width-1, self.height-1))
        linelist_x = [QLine(x, 0, x, self.height-1) for x in range(0, self.width, self.cellwidth+1)]
        linelist_y = [QLine(0, y, self.width-1, y) for y in range(0, self.height, self.cellwidth+1)]
        p.drawLines(linelist_x)
        p.drawLines(linelist_y)

    def paintEvent(self, e):
        p = QPainter(self)
        p.drawImage(QPoint(0, 0), self.board)
