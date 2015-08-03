#!/usr/bin/env python
# encoding: utf-8

import sys
from PyQt4 import QtGui,QtCore,uic

from piece import Piece
from board import Board

class Square(QtGui.QMainWindow):

    def __init__(self):
        super(Square, self).__init__()
        # ui = uic.loadUi("main.ui", self)
        self.piece = None

        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Blokus")
        # self.resize(900, 600)

        self.menubar = QtGui.QMenuBar(self)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 26))
        self.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.centralwidget = QtGui.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)

        self.redPieceGroup = QtGui.QButtonGroup(self)
        self.bluePieceGroup = QtGui.QButtonGroup(self)
        self.redCol = self.addPieceCol('red')
        self.blueCol = self.addPieceCol('blue')
        self.redPieceGroup.buttonClicked.connect(self.pickedRed)

        self.board = Board(self, 14, 14)
        self.board.dropedSignal.connect(self.droped)

        self.hbox = QtGui.QVBoxLayout(self.centralwidget)
        self.hbox.addWidget(self.board)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.redCol)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.blueCol)

    def addPieceCol(self, color):
        pieceBoard = QtGui.QDockWidget(self)
        pieceBoard.setWindowTitle(color)
        pieceBoard_content = QtGui.QWidget()
        pieceBoard.setWidget(pieceBoard_content)
        # pieceBoard.setMaximumSize(QtCore.QSize(200, 524287))
        pieceBoard.setMinimumSize(QtCore.QSize(130, 0))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        pieceBoard.setSizePolicy(sizePolicy)

        pieceBoard_scroll = QtGui.QScrollArea(pieceBoard_content)
        pieceBoard_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        pieceBoard_scroll_content = QtGui.QWidget()

        vbox = QtGui.QVBoxLayout(pieceBoard_content)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(pieceBoard_scroll)

        vbox2 = QtGui.QVBoxLayout(pieceBoard_scroll_content)
        vbox2.setContentsMargins(0, 0, 0, 0)
        pg = getattr(self, color+'PieceGroup')
        for i in range(7):
            p = Piece(pieceBoard_scroll_content, color, i)
            pg.addButton(p, i)
            vbox2.addWidget(p)
        pieceBoard_scroll.setWidget(pieceBoard_scroll_content)

        return pieceBoard

    def pickedRed(self, piece):
        self.piece = piece
        self.board.setPiece(piece)

    def droped(self):
        self.piece.setChecked(True)
        self.piece.setEnabled(False)

def main():

    square_game = QtGui.QApplication(sys.argv)

    mw = Square()
    mw.show()

    return square_game.exec_()

if __name__ == "__main__":
    sys.exit(main())

