import pygame
import os
import time


board = pygame.transform.scale(pygame.image.load(os.path.join("images","board.png")), (750,750))
chessbg = pygame.image.load(os.path.join("images","chess.bg,jpg"))
rect = (113,113,525,525)

def redraw_gamewindow():
    global win, bo
    win.blit(board,(0,0))
    bo.draw(win)
    pygame.display.update()

def click():
    #return pos(x,y) ranges of 0-7
    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0] 
            divY = y - rect[0] 
            i = int(divX/(rect[2]/8))
            j = int(divY/(rect[3]/8))
            return (i,j)
def main():
    global board
    bo = board(8,8)
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
                pos = pygame.mouse.get_pos()
                i,j = click(pos)
                #bo.board.selected[i][j].selected = True        
                bo.selected(i,j)
                

width = 750
height = 750
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Chess Game")
main()