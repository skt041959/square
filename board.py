#!/usr/bin/env python
# encoding: utf-8

from PyQt4.QtGui import QWidget,QPainter

class Board(QWidget):

    def __init__(self, parent, row, col):
        super(Board,self).__init__(parent)

        self.setFixedSize(600, 600)
        self.m_row = row
        self.m_col = col

    def paintEvent(self, e):
        p = QPainter(self)
        pass
