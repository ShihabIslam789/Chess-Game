import pygame
import os

board = pygame.transform.scale2x(pygame.image.load(os.path.join("chess_pics","board_alt.png")))
black_bishop = pygame.image.load(os.path.join("chess_pics","black_bishop.png"))
black_king = pygame.image.load(os.path.join("chess_pics","black_king.png"))
black_knight = pygame.image.load(os.path.join("chess_pics","black_knight.png"))
black_pawn = pygame.image.load(os.path.join("chess_pics","black_pawn.png"))
black_queen = pygame.image.load(os.path.join("chess_pics","black_queen.png"))
black_rook = pygame.image.load(os.path.join("chess_pics","black_rook.png"))

white_bishop = pygame.image.load(os.path.join("chess_pics","white_bishop.png"))
white_king = pygame.image.load(os.path.join("chess_pics","white_king.png"))
white_knight = pygame.image.load(os.path.join("chess_pics","white_knight.png"))
white_pawn = pygame.image.load(os.path.join("chess_pics","white_pawn.png"))
white_queen = pygame.image.load(os.path.join("chess_pics","white_queen.png"))
white_rook = pygame.image.load(os.path.join("chess_pics","white_rook.png"))

b = [black_bishop,black_king,black_knight,black_pawn, black_queen, black_rook]
w = [white_bishop,white_king,white_knight,white_pawn, white_queen, white_rook]
B =[]
W =[]

for chess_pics in b:
    B.append(pygame.transform.scale2x(chess_pics))

for chess_pics in w:
    W.append(pygame.transform.scale2x(chess_pics))

def redraw_gamewindow():
    global win
    win.blit(board,(0,0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.time(15)
        redraw_gamewindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.mousemotion:
                pass

            if event.type == pygame.mousebuttondown:
                pass

width = 600
height = 600
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Chess Game")
main()