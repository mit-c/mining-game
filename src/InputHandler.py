
import pygame as pyg
from pygame.constants import QUIT
import sys
from Physics.Acceleration import Acceleration
from Physics.PlayerPhysics import PlayerPhysics
from Physics.Velocity import Velocity

from parameters import ACCELERATION


class InputHandler:
    def __init__(self, scene, maps):
        self.movement_inputs = {
            pyg.K_w: {"func": self.handle_direction, "input": (0,-1)},
            pyg.K_a: {"func": self.handle_direction, "input": (-1, 0)},
            pyg.K_s: {"func": self.handle_direction, "input": (0, 1)},
            pyg.K_d: {"func": self.handle_direction, "input": (1, 0)},
            
        }

        self.other_inputs = {
            pyg.K_i: {"func": self.handle_inventory, "input": None},
            pyg.K_SPACE: {"func": self.handle_mine, "input": None}
        }
        self.events = None
        self.key_press_history = []
        self.scene = scene
        self.player_physics = scene.player_physics

    def get_events(self):
        
        # Gets events on this loop

        events = pyg.event.get()
        if events == []:
            return  # self.events is an array

        self.events = list(filter(self.is_valid_press, events))
        if self.events == []:  # don't want to spam terminal
            return
        
        

    def is_valid_press(self, event):
        self.handle_quit(event)
        if event.type != pyg.KEYDOWN and event.type != pyg.KEYUP:
            return False
        if event.key in self.movement_inputs:
            self.handle_movement_press(event)

        if event.key in self.other_inputs:
            self.handle_other_inputs(event)
    
    def handle_other_inputs(self, event):
        pass
        

    def handle_movement_press(self, event):
        if event.type == pyg.KEYDOWN:
            self.key_press_history.append(event.key)
   
            
        else: # keyup
            inp = self.movement_inputs[event.key]["input"]
            self.key_press_history.remove(event.key)
            if(inp[0] != 0):
                should_zero_x = True
            else:
                should_zero_x = False
            self.player_physics.acc.zero(should_zero_x)
        if self.key_press_history != []:
            handler = self.movement_inputs[self.key_press_history[-1]]["func"]
            inp = self.movement_inputs[self.key_press_history[-1]]["input"]
            handler(inp)

    def handle_quit(self, event):
        if event.type == QUIT:
            pyg.quit()
            sys.exit()

    def handle_direction(self, dir):
        dir_x, dir_y = dir
        self.player_physics.acc.set(dir_x, dir_y)
        
    def handle_other_inputs(self):
        pass

    def handle_mine(self):
        pass

    def handle_inventory(self):
        pass
