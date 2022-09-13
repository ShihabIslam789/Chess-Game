from operator import truediv
import pygame
import os
from piece import Bishop
board = pygame.transform.scale2x(pygame.image.load(os.path.join("images","board_alt.jpg")), (750,750))

black_bishop = pygame.image.load(os.path.join("images","black_bishop.png"))
black_king = pygame.image.load(os.path.join("images","black_king.png"))
black_knight = pygame.image.load(os.path.join("images","black_knight.png"))
black_pawn = pygame.image.load(os.path.join("images","black_pawn.png"))
black_queen = pygame.image.load(os.path.join("images","black_queen.png"))
black_rook = pygame.image.load(os.path.join("images","black_rook.png"))

white_bishop = pygame.image.load(os.path.join("images","white_bishop.png"))
white_king = pygame.image.load(os.path.join("images","white_king.png"))
white_knight = pygame.image.load(os.path.join("images","white_knight.png"))
white_pawn = pygame.image.load(os.path.join("images","white_pawn.png"))
white_queen = pygame.image.load(os.path.join("images","white_queen.png"))
white_rook = pygame.image.load(os.path.join("images","white_rook.png"))

b = [black_bishop,black_king,black_knight,black_pawn, black_queen, black_rook]
w = [white_bishop,white_king,white_knight,white_pawn, white_queen, white_rook]
B =[]
W =[]

for images in b:
    B.append(pygame.transform.scale(images, (55,65)))

for images in w:
    W.append(pygame.transform.scale(images(55,65)))

class Piece:
    img = -1
    rect = (113,113,525,525)
    startX = rect[0]
    startY = [1]
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def valid_moves(self):
        pass

    def isSelected(self):
        return self.Selected

    def draw(self, win):
        if self.color == "w":
            drawThis = W[self.img]
        else:
            drawThis = B[self.img]

        if self.Selected:
            pygame.draw.rect(win, (255,0,0), ())

        x = 5 + round(self.startX + (self.col*self.rect[2]/8))
        y = 5 + round(self.startY + (self.row*self.rect[3]/8))

        if self.Selected:
            pygame.draw.rect(win, (255,0,0), (x,y,55,55),2)

        win.blit(drawThis, (x,y))

class Bishop(Piece):
    img = 0

    def valid_moves(self,board):
        i = self.row
        j = self.col

        moves = []

        #top right diag
        djr = j +1
        djl = j - 1
        for di in range(i-1,-1,-1):
            if djl < 8:
                p = board[di][djl]
                if p == 0:
                    moves.append((djl,di))
                elif p.color != self.color:
                    moves. append((djl,di))
                    break
                else:
                    break

                djl += 1

class King(Piece):
    img = 1
class Knight(Piece):
    img = 2

class Pawn(Piece):
    img = 3
    def __init__(self):
        super().__init__(row,col,color)
        self.first = True
        self.queen  = False
        self.pawn = True

    def valid_moves(self, board):
        i = self.row
        j = self.col
        if i < 7:
            p = board[i+1][j]
            if p != 0:
                if self.first:

                else:
                    return:
        moves = []
        if self.first:
            if i < 7:
                p = board[i+1][j]
                if p == 0:
                    moves.append((j,i+1))
            if i < 6:
                p = board[i+2][j]
                if p == 0:
                    moves.append((j,i+2))
            
            return moves
    

class Queen(Piece):
    img = 4

    def move(self,board):
        i = self.row
        j = self.col

    moves = []

    currentCol = j
    for row in range(0,8):
        if CurrentCol = 1 >= 0:
            m1

class Rook(Piece): 
    img = 5

    def valid_moves(self,board):
            i = self.row
            j = self.col
            moves = []
        #up
            for x in range(i,-1,-1):
                p = board[i][j]
                if p == 0:
                    moves.append((j,x))
                    break

        #down
            for x in range(i,8,-1):
                p = board[i][j]
                if p == 0:
                    moves.append((j,x))
                    break


        #left
            for x in range(j,-8,-1):
                p = board[i][j]
                if p == 0:
                    moves.append((x,i))
                    break


        #right
            for x in range(j,8,-1):
                p = board[i][j]
                if p == 0:
                    moves.append((x,i))
                    break

