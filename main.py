import pygame
from engine import Game
pygame.init()
pygame.display.set_caption("Battleship")

SQUARE_SIZE= 45
MARGIN_H= SQUARE_SIZE*4
MARGIN_V = SQUARE_SIZE

WIDTH =SQUARE_SIZE*10*2 + MARGIN_H
HEIGHT = SQUARE_SIZE*10*2  + MARGIN_V
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

INDENT =10
GREY = (40,50,60)
WHITE =(255,250,250)
GREEN= (50,200,150)
RED=(250,50,100)
BLUE =(50,150,200)
ORANGE=(250,140,20)
COLORS ={"U":GREY,"M":BLUE,"H":ORANGE,"S":RED}

def draw_grid(player,left=0,top=0,search=False):
    for i in range(100):
        x= left+ i%10*SQUARE_SIZE
        y= top+i//10*SQUARE_SIZE
        square= pygame.Rect(x,y,SQUARE_SIZE,SQUARE_SIZE)
        pygame.draw.rect(SCREEN,WHITE,square,width=3)
        if search:
            x+= SQUARE_SIZE//2
            y+= SQUARE_SIZE//2
            pygame.draw.circle(SCREEN,COLORS[player.search[i]],(x,y),radius=SQUARE_SIZE//4)

def draw_ships(player,left=0,top=0):
    for ship in player.ships:
        x= left+ ship.col*SQUARE_SIZE +INDENT
        y= top+ship.row*SQUARE_SIZE +INDENT

        if ship.orientation =="h":
            width=ship.size *SQUARE_SIZE -2*INDENT
            height =SQUARE_SIZE -2*INDENT
        else:
            width=SQUARE_SIZE -2*INDENT
            height=ship.size*SQUARE_SIZE -2*INDENT
        rectangle = pygame.Rect(x,y,width,height)
        pygame.draw.rect(SCREEN,GREEN,rectangle,border_radius=15)

game =Game()


play=True
pause=False
while play:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            play=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if game.player1_turn and x<SQUARE_SIZE*10 and y <SQUARE_SIZE*10:
                row = y // SQUARE_SIZE
                col = x//SQUARE_SIZE
                index= row *10 +col
                game.make_move(index)
            elif not game.player1_turn and x>WIDTH - SQUARE_SIZE*10 and y > SQUARE_SIZE * 10 +MARGIN_V:
                row = (y-SQUARE_SIZE*10-MARGIN_V)//SQUARE_SIZE
                col=(x-SQUARE_SIZE*10 - MARGIN_H)//SQUARE_SIZE
                index = row*10 +col
                game.make_move(index)
        


        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play=False
            if event.key == pygame.K_SPACE:
                pause = not pause

    if not pause:
        SCREEN.fill(GREY)
        draw_grid(game.player1,search=True)
        draw_grid(game.player2,left=(WIDTH-MARGIN_H)//2+MARGIN_H)
        draw_grid(game.player1,top=(HEIGHT-MARGIN_V)//2+MARGIN_V)
        draw_grid(game.player2,search=True,left=(WIDTH-MARGIN_H)//2+MARGIN_H,top=(HEIGHT-MARGIN_V)//2+MARGIN_V)
        draw_ships(game.player1,top=(HEIGHT-MARGIN_V)//2+MARGIN_V)
        draw_ships(game.player2,left=(WIDTH-MARGIN_H)//2+MARGIN_H)
        pygame.display.flip()


        