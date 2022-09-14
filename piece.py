from operator import truediv
import pygame
import os
from piece import Bishop


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
    B.append(pygame.transform.scale(images, (55,55)))

for images in w:
    W.append(pygame.transform.scale(images(55,55)))

class Piece:
    img = -1
    rect = (113,113,525,525)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []
        self.king = False
        self.pawn = False

    def update_valid_moves(self):
        self.move_list = self.valid_moves(board)

    def isSelected(self):
        return self.selected

    def draw(self, win):
        if self.color == "w":
            drawThis = W[self.img]
        else:
            drawThis = B[self.img]
        x = (4 - self.col) + round(self.startX + (self.col* self.rect[2]/8))
        y = 3 + round(self.startY + (self.row * self.rect[3]/8))

        if self.selected and self.color == color:
            pygame.draw.rect(win,(255,0,0),(x,y,62,62),4)

        win.blit(drawThis,(x,y))

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def __str__(self):
        return str(self.col) + " " + str(self.row)

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

        for di in range(i-1,-1,-1):
            if djr > -1:
                p = board[di][djr]
                if p == 0:
                    moves.append((djr,di))
                elif p.color != self.color:
                    moves.append((djr,di))
                    break
                else:
                    break

                djr -=1

        # top left diagonal
        djl = j+1
        djr = j-1
        for di in range (i+1,8):
            if djl < 8:
                p = board[di][djl]
                if p == 0:
                    moves.append((djl,di))
                elif p.color != self.color:
                    moves.append((djl,di))
                    break
                else:
                    break
                djl += 1

        for di in range(i+1,8):
            if djr > -1:
                p = board[di][djr]
                if p ==0:
                    moves.append((djr,di))
                elif p.color != self.color:
                    moves.append((djr,di))
                    break
                else:
                    break
                djr -= 1
        return moves
class King(Piece):
    img = 1
class Knight(Piece):
    img = 2

class Pawn(Piece):
    img = 3
    def __init__(self,row,col,color):
        super().__init__(self,row,col,color)
        self.first = True
        self.queen  = False
        self.pawn = True

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        if self.color == 'b':
            if i < 7:
                p = board[i+1][j]
                if p != 0:
                    moves.append((j,i +1))

        # Diagonal movement
            if i < 7:
                p = board[i+1][j + 1]
                if p != 0:
                    if p.color != self.color:
                        moves.append((j+1,i+1))
            if j > 0:
                p = board[i+1][j-1]
                if p != 0:
                     if p.color != self.color:
                            moves.append((j-1, i+1))

            if self.first:
                if i < 6:
                    p = board[i+2][j]
                if p == 0:
                    if board[i+1][j] == 0:
                        moves.append((j,i+2))
                elif p.color != self.color:
                    moves.append((j,i+2))
            # White
            else:

                if i > 0:
                    p = board [i-1][j]
                    if p == 0:
                        moves.append((j,i-1))
                
                if j < 7:
                    p = board[i-1][j+1]
                    if p == 0:
                        moves.append((j,i-1))

                if j > 0:
                    p = board[i-1][j+1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append(j+1,i-1)

                if self.first:
                    if i > 1:
                        p = board[i-2][j]
                        if p == 0:
                            if board[i-1][j] == 0:
                                moves.append(j,i-2)
                        elif p.color != self.color:
                            moves.append((j,i-2))
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

