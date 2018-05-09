import pygame as pg
from pygame.locals import *
from sys import exit
import random
import os
import time
GREEN = '\033[92m'
ENDC = '\033[0m'
cls = lambda: os.system("cls")
cls()
print(GREEN + "Black Jack.\n By Finch Davis.\n Licensed to and modified by Tommy Smith.\n")
print("Welcome to a modified version of Black Jack.\n")
time.sleep(2)
print("There are a few things that need specification before going on to the actual game.\n")
time.sleep(2)
print("To 'hit', you have to click on the pile of cards.  To 'check', hit the pile of chips.")
print("Aces are equal to 1 ONLY.  Unlike normal Black Jack, YOU CAN NOT CHOOSE TO MAKE AN ACE A 1 OR AN 11.")
print("If the player and house tie, house takes advantage.")
print("Press 'enter' to continue to the game.")
input()

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.canDraw = True
        self.total = 0
        self.bust = False
    def addCard(self, cardindex):
        if cardindex >= 14 and cardindex <= 22:
            self.hand.append(cardindex - 13)
        elif cardindex >= 27 and cardindex <= 35:
            self.hand.append(cardindex - 26)
        elif cardindex >= 40 and cardindex <= 48:
            self.hand.append(cardindex - 39)
        elif cardindex in range(10,14) or cardindex in range(23,27) or cardindex in range(36,40) or cardindex in range(49,53):
            self.hand.append(10)
        else:
            self.hand.append(cardindex)
    def updateTotal(self):
        temphand = 0
        for i in self.hand:
            temphand += i
        self.total += temphand - self.total
        if self.total > 21:
            if self.name == "House":
                house.bust = True
                print(f"HOUSE BUSTED!")
                handleResult()
            else:
                self.bust = True
                print(f"{self.name} BUSTED!")
                handleResult()

class Sprite():
    def __init__(self, filepath, convertalpha):
        self.currentimg = filepath
        if not convertalpha:
            self.image = pg.image.load(filepath)
        else:
            self.image = pg.image.load(filepath).convert_alpha()
        self.rect = self.image.get_rect()
    def repos(self, x, y):
        self.rect.x = self.currentx = x
        self.rect.y = self.currenty = y
    def draw(self):
        screen.blit(self.image,self.rect)
    def reImage(self, filepath, convertalpha): # change image of sprite, same pos and size
        self.current_image = filepath
        if not convertalpha:
            self.image = pg.image.load(filepath)
        else:
            self.image = pg.image.load(filepath).convert_alpha()
        self.rect = self.image.get_rect()
        self.repos(self.currentx,self.currenty)

def drawAll(drawforreal):
    if drawforreal:
        background.draw()
        decksprite.draw()
        coins.draw()
        card1.draw()
        card2.draw()
        card3.draw()
        card4.draw()
        for card in newcards:
            card.draw()
        for housecard in newhousecards:
            housecard.draw()
        try:
            drawTotals()
        except:
            pass
        pg.display.update()

def clickHandler():
    global activecards
    mousepos = pg.mouse.get_pos()
    if decksprite.rect.collidepoint(mousepos) == 1 and player.total <= 21 and player.canDraw:
        if activecards > 2:
            for card in newcards:
                card.repos(card.currentx-100, card.currenty)
            card1.repos(card1.currentx-100, card.currenty)
            card2.repos(card2.currentx-100, card.currenty)
        newcardindex = random.randint(1,52)
        player.addCard(newcardindex)
        newcard = deck[newcardindex]
        newcardsprite = Sprite(newcard, convertalpha=True)
        newcardsprite.repos(410,270)
        newcards.append(newcardsprite)
        player.updateTotal()
        print(f"Cards in player hand: {[i for i in player.hand]}")
        activecards = activecards + 1
    if coins.rect.collidepoint(mousepos) == 1:
        player.canDraw = False
        flipDealerCard()
        global playerdone
        playerdone = True
        print(f"Cards in house hand: {[i for i in house.hand]}")
        print(f"Player's hand total: {player.total}")
        dealerTurn()

def flipDealerCard():
    card4.reImage(houseRealCard2, convertalpha=True) # flip the dealer's hidden card

def dealerTurn():
    global houseactivecards
    while house.total < 17:
        if houseactivecards > 2:
            for housecard in newhousecards:
                housecard.repos(housecard.currentx-100, housecard.currenty)
            card3.repos(card3.currentx-100,card3.currenty)
            card4.repos(card4.currentx-100,card4.currenty)
        newcardindex = random.randint(1,52)
        house.addCard(newcardindex)
        newcard = deck[newcardindex]
        newcardsprite = Sprite(newcard, convertalpha=True)
        newcardsprite.repos(410, 3)
        newhousecards.append(newcardsprite)
        house.updateTotal()
        houseactivecards = houseactivecards + 1
    print("HOUSE TURN OVER")
    print(f"HOUSE HAND: {house.hand} TOTAL: {house.total}")
    handleResult()

def handleResult():
    global drawTotals
    try:
        del drawTotals
    except:
        pass
    flipDealerCard()
    drawAll(True)
    myfont = pg.font.SysFont("Impact",40)
    scorefont = pg.font.SysFont("Impact",30)
    global drawforreal
    if house.bust:
        text = myfont.render(f"VICTORY ROYALE",True,(255, 206, 0))
        scores = scorefont.render(f"Your Total: {player.total}  House Total: {house.total}",True,(255, 206, 0))
        screen.blit(text,(195,130))
        screen.blit(scores,(145,180))
        pg.display.update()
        drawforreal = False
    elif player.bust:
        text = myfont.render("YOU LOSE",True,(203, 0, 0))
        scores = scorefont.render(f"Your Total: {player.total}  House Total: {house.total}",True,(203, 0, 0))
        screen.blit(text,(245,130))
        screen.blit(scores,(145,180))
        pg.display.update()
        drawforreal = False
    elif player.total > house.total:
        text = myfont.render(f"VICTORY ROYALE",True,(255, 206, 0))
        scores = scorefont.render(f"Your Total: {player.total}  House Total: {house.total}",True,(255, 206, 0))
        screen.blit(text,(195,130))
        screen.blit(scores,(145,180))
        pg.display.update()
        drawforreal = False
    elif player.total <= house.total:
        text = myfont.render("YOU LOSE",True,(203, 0, 0))
        scores = scorefont.render(f"Your Total: {player.total}  House Total: {house.total}",True,(203, 0, 0))
        screen.blit(text,(245,130))
        screen.blit(scores,(145,180))
        pg.display.update()
        drawforreal = False
    else:
        pass

def drawTotals():
    myfont = pg.font.SysFont("Impact",25)
    text = myfont.render(f"Player Total: {player.total}",True,(255, 206, 0))
    screen.blit(text,(230,175))

deck = {1:"aceofSpades.png", 2:"2ofSpades.png", 3:"3ofSpades.png", 4:"4ofSpades.png", 5:"5ofSpades.png", 6:"6ofSpades.png", 7:"7ofSpades.png", 8:"8ofSpades.png", 9:"9ofSpades.png", 10:"10ofSpades.png", 11:"jackofSpades.png", 12:"queenofSpades.png", 13:"kingofSpades.png",
        14:"aceofClubs.png", 15:"2ofClubs.png", 16:"3ofClubs.png", 17:"4ofClubs.png", 18:"5ofClubs.png", 19:"6ofClubs.png", 20:"7ofClubs.png", 21:"8ofClubs.png", 22:"9ofClubs.png", 23:"10ofClubs.png", 24:"jackofClubs.png", 25:"queenofClubs.png", 26:"kingofClubs.png",
        27:"aceofHearts.png", 28:"2ofHearts.png", 29:"3ofHearts.png", 30:"4ofHearts.png", 31:"5ofHearts.png", 32:"6ofHearts.png", 33:"7ofHearts.png", 34:"8ofHearts.png", 35:"9ofHearts.png", 36:"10ofHearts.png", 37:"jackofHearts.png", 38:"queenofHearts.png", 39:"kingofHearts.png",
        40:"aceofDiamonds.png", 41:"2ofDiamonds.png", 42:"3ofDiamonds.png", 43:"4ofDiamonds.png", 44:"5ofDiamonds.png", 45:"6ofDiamonds.png", 46:"7ofDiamonds.png", 47:"8ofDiamonds.png", 48:"9ofDiamonds.png", 49:"10ofDiamonds.png", 50:"jackofDiamonds.png", 51:"queenofDiamonds.png", 52:"kingofDiamonds.png"}
activecards = 2
houseactivecards = 2
playerdone = False
cardNum1 = random.randint(1,52)
realCard1 = deck[cardNum1]
cardNum2 = random.randint(1,52)
realCard2 = deck[cardNum2]
houseNum1 = random.randint(1,52)
houseRealCard1 = deck[houseNum1]
houseNum2 = random.randint(1,52)
houseRealCard2 = deck[houseNum2]
sprite_image_filename1 = (realCard1)
print(realCard1)
sprite_image_filename2 = (realCard2)
print(realCard2)
sprite_image_filename3 = (houseRealCard1)
print(houseRealCard1)
sprite_image_filename4 = 'cardBack.png'

pg.init()

newcards = []
newhousecards = []
player = Player("player")
player.addCard(cardNum1)
player.addCard(cardNum2)
player.updateTotal()

house = Player("House")
house.addCard(houseNum1)
house.addCard(houseNum2)
house.updateTotal()


pg.display.set_caption("Black Jack")
screen = pg.display.set_mode((640, 400), 0, 32)

background = Sprite("table.png", convertalpha=False)
decksprite = Sprite("deckofCards.png", convertalpha=False)
decksprite.repos(490,110)
coins = Sprite("pileofChips.png", convertalpha=False)
coins.repos(30,130)
card1 = Sprite(sprite_image_filename1, convertalpha=True)
card1.repos(210,270)
card2 = Sprite(sprite_image_filename2, convertalpha=True)
card2.repos(310,270)
card3 = Sprite(sprite_image_filename3, convertalpha=True)
card3.repos(210,3)
card4 = Sprite(sprite_image_filename4, convertalpha=True)
card4.repos(310,3)



drawforreal = True

while True:
    for event in pg.event.get():
        if event.type == MOUSEBUTTONDOWN: clickHandler()
        if event.type == QUIT:
            pg.quit()
            exit()
    drawAll(drawforreal)
