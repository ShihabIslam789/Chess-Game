import pygame
import os

board = pygame.image.load(os.path.join("images","board.png")), (750,750)

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
    B.append(pygame.transform.scale2x(images))

for images in w:
    W.append(pygame.transform.scale2x(images))

def redraw_gamewindow():
    global win
    win.blit(board,(0,0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.time(30)
        redraw_gamewindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =  False
                quit()
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