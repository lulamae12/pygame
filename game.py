
import math
from sys import exit
import random
from time import sleep
from colors import *
import pygame as pg
ReadyForRepeat = False
ReadyForRepeatA2 = False
#setup
steps = 5

pg.init()
pg.display.set_caption("centipede")
screen = pg.display.set_mode((450,700))
pg.mouse.set_visible(False)
pg.display.update()
clock = pg.time.Clock()
gameRunning = True

frame_count = 0
frame_rate = 60
start_time = 90

class Ship(object):
    def __init__(self, pos):
        self.destroyed = False
        self.health = 3
        self.image = pg.image.load("ship.png")
        self.imageRect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (28, 25))
        screen.blit(self.image,self.imageRect)
        pg.display.update()

        self.x = 200
        self.y = 565
    def getShipX(self):
        self.shipX = self.x
        print("x:",self.x)
    def controls(self):
        dist = 3
        key = pg.key.get_pressed()
        if key[pg.K_d] or key[pg.K_RIGHT]: # d key
            self.x += dist # move right
        elif key[pg.K_a] or key[pg.K_LEFT]: # a key
            self.x -= dist # move left
        if key[pg.K_ESCAPE]:
            exit()
        #right side of screen
        if self.x > 316:
            self.x = 316
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
            exit()
class Asteroid(object):
    def __init__(self, pos):
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.x = ship.x
        self.y = 100
        self.image = pg.image.load("Asteroid.png").convert()
        self.image = pg.transform.scale(self.image, (66, 71))
        self.imageRect = self.image.get_rect()
        self.imageRect = self.imageRect.move(ship.x,100)
        screen.blit(self.image,self.imageRect)
        pg.display.update()
        self.outOfBoundsLEFT = False
        self.outOfBoundsRIGHT = False
        self.outOfBoundsTOP = False
        self.outOfBoundsBOTTOM = False
    def SetSpeed(self):

        self.speed = 2

    def motion(self, screen):
        print("Speed:",self.speed)
        if self.area.contains(self.imageRect):
            screen.blit(self.image, self.imageRect)
            self.imageRect = self.imageRect.move(0,self.speed)
            screen.blit(self.image, self.imageRect)
            print(self.imageRect)
    def increaseSpeed(self):
        self.speed = self.speed + .25
        if self.speed > 9:
            self.speed = 8
    def update(self, surface):
        surface.blit(self.image, self.imageRect)
class UI(object):
    def __init__(self, pos):
        screen = pg.display.get_surface()
        self.TopCover = pg.image.load("TopCover.png").convert()#top cover for Asteroid
        self.TopCoverRect = self.TopCover.get_rect()#topcover rectangle
        self.SideCover = pg.image.load("SideCover.png").convert()
        self.SideCoverRect = self.SideCover.get_rect()
        self.SideCoverRect = self.SideCoverRect.move(350,0)
        screen.blit(self.TopCover,self.TopCoverRect)
        screen.blit(self.SideCover,self.SideCoverRect)
        pg.display.update()


    def update(self, surface):

        surface.blit(self.TopCover, self.TopCoverRect)
        screen.blit(self.SideCover,self.SideCoverRect)
class AsteroidNT(object):
    def __init__(self, pos):


        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.x = random.randrange(1,316)
        self.y = 0
        self.image = pg.image.load("asteroid.png")
        self.image = pg.transform.scale(self.image, (66, 71))
        self.imageRect = self.image.get_rect()

        self.imageRect = self.imageRect.move(self.x,0)
        screen.blit(self.image,self.imageRect)
        pg.display.update()
        self.outOfBoundsLEFT = False
        self.outOfBoundsRIGHT = False
        self.outOfBoundsTOP = False
        self.outOfBoundsBOTTOM = False
    def SetSpeed(self):

        self.speed = 2

    def motion(self, screen):

        print("Speed:",self.speed)
        if self.area.contains(self.imageRect):
            screen.blit(self.image, self.imageRect)
            self.imageRect = self.imageRect.move(0,self.speed)
            screen.blit(self.image, self.imageRect)
            print(self.imageRect)



    def increaseSpeed(self):
        self.speed = self.speed + .25
        if self.speed > 9:
            self.speed = 8
    def update(self, surface):

        surface.blit(self.image, self.imageRect)
class Timer(object):
    def __init__(self, pos):
        self.TimerFont = pg.font.Font("retro1.ttf", 20)
        screen = pg.display.get_surface()
    def Calculate(Self):
        self.total_time = frame_count // frame_rate#Calculate total amount of time in seconds
        self.minutes = self.total_time // 60 #get minutes(as if they would even be used)
        self.seconds = self.total_time % 60 #use modulus to get remaining seconds

        self.timerOutputString = "Time: {0:02}:{1:02}".format(minutes, seconds) #outputs with zeros
    def displayTimer(Self):
        self.timerTime = TimerFont.render(output_string, True, BLACK)
        screen.blit(text, [250, 250])

def update():#update group
    asteroid1.update(screen)
    asteroid2.update(screen)
    ship.update(screen)
    ui.update(screen)
    pg.display.update()
def moveGroup():
    asteroid1.motion(screen)
    asteroid2.motion(screen)
def collisionCheck():
    ship.collisionCheck(asteroid1)
    ship.collisionCheck(asteroid2)


def main():
    asteroid1.SetSpeed()
    asteroid2.SetSpeed()

    while gameRunning: #main loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
                gameRunning == False


        collisionCheck()

        moveGroup()
        update()
        ship.getShipX()
        ship.controls() # handle the keys
        screen.fill(BLACK)


        """keeps ship on screen"""
        if asteroid1.area.contains(asteroid1.imageRect):
            ReadyForRepeat = False
        else:
            ReadyForRepeat = True

        if asteroid2.area.contains(asteroid2.imageRect):
            ReadyForRepeatA2 = False
        else:
            ReadyForRepeatA2 = True

        if ReadyForRepeat == True:

            asteroid1.increaseSpeed()
            asteroid1.__init__(object)
            asteroid1.motion(screen)

            ReadyForRepeat = False

        if ReadyForRepeatA2 == True:

            asteroid2.increaseSpeed()
            asteroid2.__init__(object)
            asteroid2.motion(screen)

            ReadyForRepeatA2 = False

ui = UI(object)
ship = Ship(object)
asteroid1 = Asteroid(object)
asteroid2 = AsteroidNT(object)
main()
