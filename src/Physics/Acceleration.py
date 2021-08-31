
from TwoDim import TwoDim
from parameters import *

class Acceleration(TwoDim):
        def set(self, dir_x=0, dir_y=0):
            if dir_x != 0:
                self.x= dir_x
            if dir_y != 0:
                self.y = dir_y 
            
            self.set_tuple()
            
            self.normalise_tuple()
            self.x = self.tuple[0]
            self.y = self.tuple[1]

        def zero(self,should_zero_x):
            if should_zero_x:
                self.x = 0
            else:
                self.y = 0
            self.set_tuple()

            