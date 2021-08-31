
from TwoDim import TwoDim
from parameters import *

class Velocity(TwoDim):
    def calc_new_speed(self, acc):
        self.x = self.x +  acc.x* DT # v = u+at
        self.y = self.y +  acc.y* DT
        self.set_tuple()
        # should not be normalised