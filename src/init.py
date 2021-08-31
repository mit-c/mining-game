# This file is responsible for initializing stuff
import pygame as pyg
from Physics.PlayerPhysics import PlayerPhysics
from Physics.Position import Position
from Physics.Scene import Scene
from parameters import *
def game():
    #sprites, sounds, levels = load("sounds")
    pyg.init()
    screen = pyg.display.set_mode((WIDTH, HEIGHT))
    scene = Scene(None, PlayerPhysics(pos=Position(WIDTH//2, HEIGHT//2)))
    return screen, scene

def load():
    pass
