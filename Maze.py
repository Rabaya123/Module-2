import pygame
import random
import time

WIDTH = 800
HEIGHT = 800
FPS = 30

# initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()
white = [255, 255, 255]
black = [0,0,0]
screen.fill(white)
pygame.display.update()

running = True

def drawGrid(n):
    pygame.draw.line(screen,black,[0, 0],[0,WIDTH],2)
    pygame.draw.line(screen,black,[0, 0],[HEIGHT,0],2)
    pygame.draw.line(screen,black,[HEIGHT-2, 0],[HEIGHT-2,WIDTH-2],2)
    pygame.draw.line(screen,black,[0, WIDTH-2],[HEIGHT-2,WIDTH-2],2)
    for y in range(int(HEIGHT/n),HEIGHT-1, int(HEIGHT/n)):
        for x in range(0,WIDTH-1, int(WIDTH/n)):
            if (x > ((WIDTH-1) - int(WIDTH/n))):
                pygame.draw.line(screen,black,[x+int(WIDTH/n), y],[x+int(WIDTH/n),y-int(HEIGHT/n)],2)

            elif (random.randrange(1,11)>5):
                pygame.draw.line(screen,black,[x, y],[x+int(WIDTH/n),y],2)
            else:
                pygame.draw.line(screen,black,[x+int(WIDTH/n), y],[x+int(WIDTH/n),y-int(HEIGHT/n)],2)

            pygame.display.update()
# DRAW TOP LINE
# pygame.draw.line(screen,black,[x, y],[x+int(WIDTH/n),y],2)
# DRAW RIGHT LINE
# pygame.draw.line(screen,black,[x, y],[x+int(WIDTH/n),y],2)
#

print("What is the size of the grid?")
n = input()
n = int(n)
drawGrid(n)

while running:
    # keep running at the at the right speed
    clock.tick(FPS)


    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
