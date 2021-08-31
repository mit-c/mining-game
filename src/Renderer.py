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
        # We want to translate our map by 
    
        

    def paint(self):
        self.screen.fill(pyg.Color(0,0,0,0))
        self.paint_background()
        self.paint_collision_map()
        self.paint_entities()
        self.paint_player()
        pyg.display.flip()
        
    def paint_background(self):
        background_tiles = self.sprites.image_dict["tiles"] # there are 8 tiles
        player_pos = self.scene.player_physics.pos
        tile = self.sprites.get_index("tiles", 0)
        initial_x = (-player_pos.x % CELL_WIDTH) + WIDTH // 2
        initial_y = (-player_pos.y % CELL_WIDTH) + HEIGHT // 2
        for i in range(-15,15):
            
            for j in range(-15,15):
                x = initial_x + i * CELL_WIDTH
                y = initial_y + j * CELL_WIDTH
                self.screen.blit(tile,(x, y))



                
            

    def paint_entities(self):
        pass

    def paint_player(self):
        pyg.draw.circle(self.screen, (250,0,0), (WIDTH // 2, HEIGHT // 2),10)
        
    def paint_collision_map(self):
        # We only want to choose random numbers once
        
        sprites = self.sprites
        count = 0
        self.maps["collision_map"].transform_by_player_pos(self.scene.player_physics.pos)
        col_dict = self.maps["collision_map"].transformed_dict
        
        for pos in col_dict:
            
            for char in (col_dict[pos]):
                if not char == "|":
                    continue
                
                self.screen.blit(sprites.get_index("rocks",count), pos.get_tuple())
                count += 1
