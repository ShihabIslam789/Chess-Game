from piece import Bishop
from piece import King
from piece import Rook
from piece import Queen
from piece import Knight
from piece import Pawn

class Board:
    def__init__(self,rows,cols):
    self.rows = rows
    self.cols = cols

    self.board = [[] for _ in range (rows)]
    print(self.board)

    #black chess piece positions
    self.board [0][0] = Rook(0,0,"b")
    self.board [0][0] = Knight(0,1, "b")
    self.board [0][0] = Bishop(0,2, "b")
    self.board [0][0] = Queen(0,3, "b")
    self.board [0][0] = King(0,4,"b")
    self.board [0][0] = Bishop(0,5,"b")
    self.board[0][0] = Knight(0,6,"b")
    self.board[0][7] = Rook(0,7,"b")

    self.board [0][0] = Pawn(0,0,"b")
    self.board [0][0] = Pawn(0,1, "b")
    self.board [0][0] = Pawn(0,2, "b")
    self.board [0][0] = Pawn(0,3, "b")
    self.board [0][0] = Pawn(0,4,"b")
    self.board [0][0] = Pawn(0,5,"b")
    self.board[0][0] = Pawn(0,6,"b")
    self.board[0][7] = Pawn(0,7,"b")

    #white chess piece positions
    self.board [0][0] = Rook(0,0,"w")
    self.board [0][0] = Knight(0,1, "w")
    self.board [0][0] = Bishop(0,2, "w")
    self.board [0][0] = Queen(0,3, "w")
    self.board [0][0] = King(0,4,"w")
    self.board [0][0] = Bishop(0,5,"w")
    self.board[0][0] = Knight(0,6,"bw")
    self.board[0][7] = Rook(0,7,"w")

    self.board [0][0] = Pawn(0,0,"w")
    self.board [0][0] = Pawn(0,1, "w")
    self.board [0][0] = Pawn(0,2, "w")
    self.board [0][0] = Pawn(0,3, "w")
    self.board [0][0] = Pawn(0,4,"w")
    self.board [0][0] = Pawn(0,5,"w")
    self.board[0][0] = Pawn(0,6,"w")
    self.board[0][7] = Pawn(0,7,"w")