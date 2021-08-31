from math import ceil
import pygame as pyg
from pygame.event import set_blocked

from parameters import CELL_WIDTH, HEIGHT, WIDTH
class Renderer:
    def __init__(self, screen, scene, maps, sprites) -> None:
        self.scene = scene
        self.screen = screen
        self.maps = maps
        self.sprites = sprites
        
    
        

    def paint(self):
        self.paint_background()
        self.paint_collision_map()
        self.paint_entities()
        self.paint_player()
        pyg.display.flip()
        
    def paint_background(self):
        background = pyg.Surface((WIDTH,HEIGHT))
        background = background.convert()
        background.fill((150,10,150)) # red
        self.screen.blit(background, (0,0))
    def paint_entities(self):
        pass

    def paint_player(self):
        # todo change so play in centre
        player_pos = self.scene.player_physics.pos
        pyg.draw.circle(self.screen, (250,0,0), (player_pos.x, player_pos.y),10)
        
    def paint_collision_map(self):
        # We only want to choose random numbers once
        
        sprites = self.sprites
        count = 0
        for j,line in enumerate(self.maps["collision_map"].array):
            for i,char in enumerate(line):
                if not char == "|":
                    continue
                self.screen.blit(sprites.get_index("rocks",count), (i*CELL_WIDTH, j*CELL_WIDTH))
                count += 1
