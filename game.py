
import math
import pickle
from sys import exit
import random
from time import sleep
from gamelauncher import *
from colors import *
import pygame as pg
ReadyForRepeat = False
ReadyForRepeatA2 = False
#setup
steps = 1
feet = 0
signinMenu()
pg.init()

pg.display.set_caption("SPACE JAM: Beta")
screen = pg.display.set_mode((450,700))
pg.display.update()
clock = pg.time.Clock()
clock.tick(60)

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
            finalHeight = ui.HeightScore()
            finalHeightfixed = float(finalHeight) -.3
            finalHeightfixed = str(finalHeightfixed)
            finalHeightfixed = finalHeightfixed[0:5]
            print("FH",finalHeightfixed)
            getScore(finalHeightfixed)
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
        self.speed = 1
    def motion(self, screen):

        if self.area.contains(self.imageRect):
            screen.blit(self.image, self.imageRect)
            self.imageRect = self.imageRect.move(0,self.speed)
            screen.blit(self.image, self.imageRect)
    def increaseSpeed(self):
        self.speed = self.speed + .25
        if self.speed > 9:
            self.speed = 8
        return self.speed
    def update(self, surface):
        surface.blit(self.image, self.imageRect)
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
        self.speed = 1
    def motion(self, screen):
        if self.area.contains(self.imageRect):
            screen.blit(self.image, self.imageRect)
            self.imageRect = self.imageRect.move(0,self.speed)
            screen.blit(self.image, self.imageRect)
    def increaseSpeed(self):
        self.speed = self.speed + .25
        if self.speed > 9:
            self.speed = 8
    def update(self, surface):
        surface.blit(self.image, self.imageRect)
class UI(object):
    def __init__(self, pos):
        screen = pg.display.get_surface()
        self.counterFont = pg.font.Font('Alien-Encounters-Bold.ttf', 30)
        self.TopCover = pg.image.load("TopCover.png").convert()#top cover for Asteroid
        self.TopCoverRect = self.TopCover.get_rect()#topcover rectangle
        self.SideCover = pg.image.load("SideCover.png").convert()
        self.SideCoverRect = self.SideCover.get_rect()
        self.SideCoverRect = self.SideCoverRect.move(350,0)
        self.smallTopCover = pg.image.load("smallTopCover.png").convert()#cover for behind text
        self.smallTopCoverRect = self.smallTopCover.get_rect()
        self.smallTopCoverRect = self.smallTopCoverRect.move(200,0)
        screen.blit(self.TopCover,self.TopCoverRect)
        screen.blit(self.SideCover,self.SideCoverRect)
        screen.blit(self.smallTopCover,self.smallTopCoverRect)
        pg.display.update()
    def HeightScore(self):
        global feet
        feet = feet+.1
        self.numForCounter = str(feet)
        self.numForCounter = self.numForCounter[0:5]

        return self.numForCounter
        print(self.numForCounter)
    def counterFT(self):
        counterSurface = self.counterFont.render(("Altitude: " + self.numForCounter + " Km."), False, RED)#render font
        self.TopCover.blit(self.smallTopCover,(40,-20))#add background for text so it doesnt overlap
        self.smallTopCover.fill(BLACK)#fill background for text black to "clear it"
        self.smallTopCover.blit(counterSurface,(0,40))#update

    def update(self, surface):
        surface.blit(self.TopCover, self.TopCoverRect)
        surface.blit(self.SideCover,self.SideCoverRect)

class gameMenu(object):
    def __init__(self, pos):

        screen = pg.display.get_surface()
        self.buttonX = False #menuButton002.png
        self.buttonLine = True #menuButton001.png
        self.menuButton = pg.image.load("menuButton002.png")# 2 line button
        self.menuButton = pg.transform.scale(self.menuButton, (75, 75))
        self.menuButtonRect = self.menuButton.get_rect()
        self.menuButtonRect = self.menuButtonRect.move(370,1)
        screen.blit(self.menuButton, self.menuButtonRect)
        pg.display.update()
    def button(self, surface):
        if pg.mouse.get_pressed()[0]:
            pos = pg.mouse.get_pos()
            if self.menuButtonRect.collidepoint(pos) == 1:
                self.menuButton = pg.image.load("menuButton002.png")#button x
                self.menuButtonRect = self.menuButton.get_rect()
                self.menuButtonRect = self.menuButtonRect.move(370,1)
                self.menuButton = pg.transform.scale(self.menuButton, (75, 75))
                screen.blit(self.menuButton, self.menuButtonRect)
                exit()
    def update(self, surface):
        surface.blit(self.menuButton, self.menuButtonRect)
class Background():
    def __init__(self):
        self.backgroundImage = pg.image.load("background.png").convert()
        self.backgroundImageRect = self.backgroundImage.get_rect()
        self.backgroundX = 0
        self.backgroundY = -6000
        self.speed = .5
        screen.blit(self.backgroundImage, self.backgroundImageRect)
        pg.display.update()
    def move(self):
        self.backgroundY += self.speed
    def update(self, surface):
        surface.blit(self.backgroundImage, (self.backgroundX, self.backgroundY))

def update():#update group
    background.update(screen)
    asteroid1.update(screen)
    asteroid2.update(screen)
    ship.update(screen)
    ui.update(screen)
    gameMenu.update(screen)

    #add above
    pg.display.update()
def moveGroup():

    asteroid1.motion(screen)
    asteroid2.motion(screen)

def collisionCheck():
    ship.collisionCheck(asteroid1)
    ship.collisionCheck(asteroid2)


def main():
    global feet
    gameRunning = True

    asteroid1.SetSpeed()
    asteroid2.SetSpeed()

    while gameRunning: #main loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
                gameRunning == False
        collisionCheck()
        background.move()
        moveGroup()
        update()
        ship.getShipX()
        ship.controls() # handle the keys
        screen.fill(BLACK)
        ui.HeightScore()
        ui.counterFT()
        gameMenu.button(screen)
        print(clock.tick())
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


background = Background()
ship = Ship(object)
asteroid1 = Asteroid(object)
asteroid2 = AsteroidNT(object)
gameMenu = gameMenu(object)
ui = UI(object)


main()
