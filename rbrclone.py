
import math, sys
import pygame as pg
from colors import *

#setup
steps = 5

pg.init()
pg.display.set_caption("centipede")
screen = pg.display.set_mode((600,600))
pg.mouse.set_visible(False)
pg.display.update()
clock = pg.time.Clock()
gameRunning = True


class Ship(object):
    def __init__(self, pos):
        self.destroyed = False
        self.health = 1
        self.image = pg.image.load("ship.gif")
        self.imageRect = self.image.get_rect()

        screen.blit(self.image,self.imageRect)
        pg.display.update()
        self.x = 100
        self.y = 100

    def getMousePos(self):
        (self.MouseX, self.MouseY) = pg.mouse.get_pos()
        print(self.MouseX, self.MouseY)
    def goToMouse(self):
        self.x = self.MouseX
        self.y = self.MouseY

        #right side of screen
        if self.x > 585:
            self.x = 585
        #bottom of screen
        if self.y > 587:
            self.y = 587


    def controls(self):

        key = pg.key.get_pressed()

        if key[pg.K_ESCAPE]:
            sys.exit()

    def update(self, surface):
        surface.blit(self.image, (self.x, self.y))
    def keepinbounds(self):
        if self.x < 3:
            self.x == 3
    def collisionCheck(self, sprite1, sprite2):
        col = self.imageRect.colliderect(sprite1, sprite2)
        if col == True:
            print("hit")

class Asteroid(object):
    def __init__(self, pos):
        self.x = 100
        self.y = 100
        self.image = pg.image.load("Asteroid.png")

        self.image = pg.transform.scale(self.image, (66, 71))
        self.imageRect = self.image.get_rect()
        screen.blit(self.image,self.imageRect)
        pg.display.update()
        self.outOfBoundsLEFT = False
        self.outOfBoundsRIGHT = False
        self.outOfBoundsTOP = False
        self.outOfBoundsBOTTOM = False
    def keepinbounds(self):
        #left
        if self.x < 3:
            self.x = 3
            self.outOfBoundsLEFT = True
        elif self.x > 3:
            self.outOfBoundsLEFT = False
        #right
        if self.x > 583:
            self.x = 583
            self.outOfBoundsRIGHT = True
        elif self.x < 583:
            self.outOfBoundsRIGHT = False
        #bottom
        if self.y > 486 :
            self.y = 486
            self.outOfBoundsBOTTOM = True
        elif self.y < 486:
            self.outOfBoundsBOTTOM = False
        #top
        if self.y < 0:
            self.y = 0
            self.outOfBoundsTOP = True
        elif self.y > 0:
            self.outOfBoundsTOP = False
    def update(self, surface):
        surface.blit(self.image, self.imageRect)

ship = Ship(object)
asteroid1 = Asteroid(object)


"""main loop"""
while gameRunning: #main loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            gameRunning == False
        ship.collisionCheck(ship.imageRect, asteroid1.image)
    ship.getMousePos()
    ship.goToMouse()
    ship.controls() # handle the keys
    screen.fill(BLACK)
    asteroid1.update(screen)
    ship.update(screen) # draw the bird to the screen
    pg.display.update()
    ship.keepinbounds

    """keeps ship on screen"""
    #left
