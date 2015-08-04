#!/usr/bin/env python
# encoding: utf-8

from PyQt4.QtGui import QWidget,QPainter,QColor,QImage
from PyQt4.QtCore import QPoint,QSize,QLine,QRect,Qt,pyqtSignal

from piece import Piece

class Board(QWidget):

    dropedSignal = pyqtSignal(str, int, name='piece_dropped')

    def __init__(self, parent, row, col):
        super(Board,self).__init__(parent)

        self.x = -1
        self.y = -1
        self.piece = None
        self.row = row
        self.col = col

        self.cellwidth = 50
        self.linewidth = 1

        self.width = self.cellwidth*col + self.linewidth*(col+1)
        self.height = self.cellwidth*row + self.linewidth*(row+1)

        self.setFixedSize(self.width, self.height)

        self.board = QImage(self.width, self.height, QImage.Format_ARGB32)
        self.pieces = QImage(self.width, self.height, QImage.Format_ARGB32)

        p = QPainter(self.board)
        p.setBrush(QColor(255, 255, 255, 255))
        p.drawRect(QRect(0, 0, self.width-1, self.height-1))
        linelist_x = [QLine(x, 0, x, self.height-1) for x in range(0, self.width, self.cellwidth+1)]
        linelist_y = [QLine(0, y, self.width-1, y) for y in range(0, self.height, self.cellwidth+1)]
        p.drawLines(linelist_x + linelist_y)

        self.pieces.fill(0x000000FF)

        self.setMouseTracking(True)

    def setPiece(self, p):
        self.piece = p

    def paintEvent(self, e):
        p = QPainter(self)
        p.drawImage(QPoint(0, 0), self.board)
        p.drawImage(QPoint(0, 0), self.pieces)

        if self.piece:
            # print(self.x, self.y)
            p.drawImage(QPoint((self.x-2)*51, (self.y-2)*51), self.piece.getImage())

    def mouseMoveEvent(self, e):
        x,y = e.pos().x(), e.pos().y()

        if self.piece and (x//51 != self.x or y//51 != self.y):
            self.x = x//51
            self.y = y//51
            self.update()

    def mousePressEvent(self, e):
        if self.piece:
            if e.button() == Qt.LeftButton:
                p = QPainter(self.pieces)
                p.drawImage(QPoint((self.x-2)*51, (self.y-2)*51), self.piece.getImage())
                self.update()
                self.dropedSignal.emit(self.piece.color, self.piece.shape)
                self.piece = None

            elif e.button() == Qt.RightButton:
                self.piece.flip()
                self.update()

    def wheelEvent(self, e):
        if self.piece:
            if e.delta() > 0:
                self.piece.rotate(1)
            else:
                self.piece.rotate(-1)
            self.update()

