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

    def move(self):
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

class King(Piece):
    img = 1
class Knight(Piece):
    img = 2
class Pawn(Piece):
    img = 3
    def__init__(self):
        super().__init__(row,col,color)
        self.first = True
        self.queen  = False

    def move(self, board):
    i = self.row
    j = self.col
    
    

class Queen(Piece):
    img = 4

    def move(self,board):
    pass

class Rook(Piece): 
    img = 5