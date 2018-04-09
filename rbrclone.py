
import math, sys, random
import pygame as pg
from colors import *
ReadyForRepeat = False
#setup
steps = 5
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BALL_SIZE = 71
pg.init()
pg.display.set_caption("centipede")
screen = pg.display.set_mode((600,600))
pg.mouse.set_visible(False)
pg.display.update()
clock = pg.time.Clock()
gameRunning = True
clock.tick(60)

class Ship(object):
    def __init__(self, pos):
        self.destroyed = False
        self.health = 1
        self.image = pg.image.load("ship.gif")
        self.imageRect = self.image.get_rect()
        screen.blit(self.image,self.imageRect)
        pg.display.update()


        self.x = 300
        self.y = 465
    def getShipX(self):
        self.shipX = self.x
        print("x:",self.x)
    def controls(self):
        dist = 3
        key = pg.key.get_pressed()
        if key[pg.K_d]: # d key
            self.x += dist # move right

        elif key[pg.K_a]: # a key
            self.x -= dist # move left
        if key[pg.K_ESCAPE]:
            sys.exit()
        #right side of screen
        if self.x > 585:
            self.x = 585
        #left of screen
        if self.x < 0:
            self.x = 0
    def update(self, surface):
        surface.blit(self.image, (self.x, self.y))
    def keepinbounds(self):
        if self.x < 3:
            self.x == 3
    def collisionCheck(self, asteroid):
        col = asteroid.imageRect.collidepoint(self.x, self.y)
        if col == True:
            print("hit")
            sys.exit()
class Asteroid(object):
    def __init__(self, pos):


        screen = pg.display.get_surface()
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.x = ship.x
        self.y = 0
        self.image = pg.image.load("Asteroid.png")
        self.image = pg.transform.scale(self.image, (66, 71))
        self.imageRect = self.image.get_rect()
        self.imageRect = self.imageRect.inflate(-10,-10)
        self.imageRect = self.imageRect.move(ship.x,0)
        screen.blit(self.image,self.imageRect)
        pg.display.update()
        self.outOfBoundsLEFT = False
        self.outOfBoundsRIGHT = False
        self.outOfBoundsTOP = False
        self.outOfBoundsBOTTOM = False



    def motion(self, screen):

        if self.area.contains(self.imageRect):
            screen.blit(self.image, self.imageRect)
            self.imageRect = self.imageRect.move(0,5)
            screen.blit(self.image, self.imageRect)
            pg.display.update()
            print(self.imageRect)

            print("fasle")
        else:
            print("true")

    def update(self, surface):
        surface.blit(self.image, self.imageRect)





def main():
    while gameRunning: #main loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
                gameRunning == False
        ship.collisionCheck(asteroid1)


    
        ship.getShipX()
        ship.controls() # handle the keys
        screen.fill(BLACK)
        asteroid1.update(screen)
        ship.update(screen)
        pg.display.update()
        ship.keepinbounds
        asteroid1.motion(screen)
        """keeps ship on screen"""
        if asteroid1.area.contains(asteroid1.imageRect):
            ReadyForRepeat = False
        else:
            ReadyForRepeat = True
        if ReadyForRepeat == True:
            asteroid1.__init__(object)
            asteroid1.update(screen)
            pg.display.update()
            asteroid1.motion(screen)
ship = Ship(object)
asteroid1 = Asteroid(object)
main()
