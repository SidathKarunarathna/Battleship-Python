import pygame

pygame.init()
pygame.display.set_caption("Battleship")

SQUARE_SIZE= 45
MARGIN_H= SQUARE_SIZE*4
MARGIN_V = SQUARE_SIZE

WIDTH =SQUARE_SIZE*10*2 + MARGIN_H
HEIGHT = SQUARE_SIZE*10*2  + MARGIN_V
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

GREY = (40,50,60)
WHITE =(255,250,250)

def draw_grid(left=0,top=0):
    for i in range(100):
        x= left+ i%10*SQUARE_SIZE
        y= top+i//10*SQUARE_SIZE
        square= pygame.Rect(x,y,SQUARE_SIZE,SQUARE_SIZE)
        pygame.draw.rect(SCREEN,WHITE,square,width=3)



play=True
pause=False
while play:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            play=False
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play=False
            if event.key == pygame.K_SPACE:
                pause = not pause

    if not pause:
        SCREEN.fill(GREY)
        draw_grid(left=20,top=20)
        draw_grid(left=(WIDTH-MARGIN_H)//2+MARGIN_H-20,top = 20)
        draw_grid(left=20,top=(HEIGHT-MARGIN_V)//2+MARGIN_V)
        draw_grid(left=(WIDTH-MARGIN_H)//2+MARGIN_H-20,top=(HEIGHT-MARGIN_V)//2+MARGIN_V)
        pygame.display.flip()


        