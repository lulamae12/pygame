#tetris.py
import os, random, sys, time
from colors import *

try:
    import pygame as pg
except ImportError:
    print("ERROR: Pygame is not installed. Installing now.")
    subprocess.call("py -3 -m pip install pygame")
    import pygame as pg
x = 100# xcoord for window
y = 100# y coord for window
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)#sets window postion
FPS = 25 #frameRate
WINDOWWIDTH = 640#width of window
WINDOWHEIGHT = 480#height of window
BOXSIZE = 20 #size of each "box"
PLAYSPACEWIDTH = 10 #area where game is played
PLAYSPACEHEIGHT = 20#area where game is played
BLANK = '.' #blank spot. used to show templates where there is no block
MOVESIDEWAYSSPEED = 0.15
MOVEDOWNSPEED = 0.1
XMARGIN = int((WINDOWWIDTH - PLAYSPACEWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (PLAYSPACEHEIGHT * BOXSIZE) - 5
BORDERCOLOR = BLUE
BACKGROUNDCOLOR = BLACK
TEXTCOLOR = WHITE
TEXTBACKGROUNDCOLOR = GRAY
MAINCOLORS = (BLUE, GREEN, RED, YELLOW)
MAINCOLORSLIGHT = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(MAINCOLORS) == len(MAINCOLORSLIGHT) #try and give each color its light equivilant
TEMPLATEWIDTH = 5#template size
TEMPLATEHEIGHT = 5

S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',#TEMPLATE FOR s PIECES
                     '.OO..',#
                     '.....'],
                    ['.....',
                     '..O..',#
                     '..OO.',#s peice rotated
                     '...O.',#
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',#TEMPLATE FOR z PIECES
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',#rotated z peice
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',#TEMPLATE FOR i PIECES
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',#rotated
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',#TEMPLATE FOR square or o PIECES
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',#rotated 1
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',#rotated 2
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',#rotated 3
                     '.OO..',
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',#mirrord j shape
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',#rotated 1
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',#rotated 2
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',#rotated 3
                     '..O..',
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',#t template
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',#rotated 1
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',#rotated 2
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',#rotated 3
                     '..O..',
                     '.....']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}
def main():
    global FPSCLOCK, SCREEN, BASICFONT, BIGFONT
    pg.init()#start pygame
    FPSCLOCK = pg.time.Clock()#start fps Clock
    SCREEN = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))#set window size
    NORMALFONT = pg.font.Font("Enter-The-Grid.ttf", 18)#normal text font
    LARGEFONT = pg.font.Font("Enter-The-Grid.ttf", 100)#large text font
    pg.display.set_caption("Just your average Tetris clone.")#set display caption
    showStartScreen("Just your average Tetris clone.")#call start SCREEN
    
