import pygame
import sys
from pygame.locals import *
pygame.init()
# setup window
size = (600, 300)
form = pygame.display.set_mode(size)
white = (255, 255, 255)
catimg = pygame.image.load("cat.png")
x = 0
y = 0
p = (x, y)
h = 'phai'
clock = pygame.time.Clock()
while True:
    form.fill(white)
    form.blit(catimg, p)
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == 275:
                x += 10
                p = (x, y)
                form.blit(catimg, p)
            if e.key == 276:
                x -= 10
                p = (x, y)
                form.blit(catimg, p)
            if e.key == 274:
                y += 10
                p = (x, y)
                form.blit(catimg, p)
            if e.key == 273:
                y -= 10
                p = (x, y)
                form.blit(catimg, p)

    pygame.display.update()
