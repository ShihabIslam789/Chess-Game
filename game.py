
import pygame
import os
from client import  network
import time
import pickle
pygame.font.init()


board = pygame.transform.scale(pygame.image.load(os.path.join("images","board.png")), (750,750))
chessbg = pygame.image.load(os.path.join("images","chess.bg,jpg"))
rect = (113,113,525,525)

turn = "w"

def menu_screen(win, name):
    global bo, chessbg
    run = True
    offline = False

    while run:
        win.blit(chessbg,(0,0))
        small_font = pygame.font.SysFont("comicsans", 50)

        if offline:
            off = small_font.render("Server Offline, Try again Later...",1, (255,0,0))
            win.blit(off, (width / 2 - off.get_width()/ 2, 500))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                offline = False
                try:
                    bo = connect()
                    run = False
                    main()
                    break
                except:
                    print("Server Offline")
                    offline = True

def redraw_gamewindow(win,bo,p1,p2,color, ready):
    win.blit(board,(0,0))
    bo.draw(win, color)

    formatTime1 = str(int(p1//60)) + ":" + str(int(p1%60))
    formatTime2 = str(int(p2 // 60)) + ":" + str(int(p2 % 60))
    if int(p1%60) < 10:
        formatTime1 = formatTime1[:-1] + "0" + formatTime1[-1]
    if int(p2%60) < 10:
        formatTime2 = formatTime2[:-1] + "0" + formatTime2[-1]

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