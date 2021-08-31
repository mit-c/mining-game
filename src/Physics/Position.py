from TwoDim import TwoDim
from parameters import *

class Position(TwoDim):
    def calc_pos(self, vel_x, vel_y, scene):
        pos_x, pos_y = scene.collision_detection(self,vel_x, vel_y)
        self.x = pos_x
        self.y = pos_y
        self.set_tuple()