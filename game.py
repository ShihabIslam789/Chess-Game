
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

    font = pygame.font.SysFont("comicsans", 30)
    try:
        txt = font.render(bo.p1Name + "\'s Time: " + str(formatTime2), 1, (255, 255, 255))
        txt2 = font.render(bo.p2Name + "\'s Time: " + str(formatTime1), 1, (255,255,255))
    except Exception as e:
        print(e)
    win.blit(txt, (520,10))
    win.blit(txt2, (520, 700))

    txt = font.render("Press q to Quit", 1, (255, 255, 255))
    win.blit(txt, (10, 20))

    if color == "s":
        txt3 = font.render("SPECTATOR MODE", 1, (255, 0, 0))
        win.blit(txt3, (width/2-txt3.get_width()/2, 10))
    
    if not ready:
        show = "Waiting for Player"
        if color == "s":
            show = "Waiting for Players"
        font = pygame.font.SysFont("comicsans", 80)
        txt = font.render(show, 1, (255, 0, 0))
        win.blit(txt, (width/2 - txt.get_width()/2, 300))

    if not color == "s":
        font = pygame.font.SysFont("comicsans", 30)
        if color == "w":
            txt3 = font.render("YOU ARE WHITE", 1, (255, 0, 0))
            win.blit(txt3, (width / 2 - txt3.get_width() / 2, 10))
        else:
            txt3 = font.render("YOU ARE BLACK", 1, (255, 0, 0))
            win.blit(txt3, (width / 2 - txt3.get_width() / 2, 10))

        if bo.turn == color:
            txt3 = font.render("YOUR TURN", 1, (255, 0, 0))
            win.blit(txt3, (width / 2 - txt3.get_width() / 2, 700))
        else:
            txt3 = font.render("THEIR TURN", 1, (255, 0, 0))
            win.blit(txt3, (width / 2 - txt3.get_width() / 2, 700))

    pygame.display.update()

def end_screen(win,text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(text,1,(255,0,0))
    win.blit(txt, (width/2 - txt.get_width()/2, 300))
    pygame.display.update()

    pygame.time.set_timer(pygame.USEREVENT + 1, 3000)


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