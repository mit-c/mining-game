
from Physics.Acceleration import Acceleration
from Physics.Position import Position

from Physics.Velocity import Velocity

class PhysicsInterface:
    def __init__(self,pos=Position(), vel=Velocity(), acc=Acceleration()) -> None:
        self.pos = pos
        self.vel = vel
        self.acc = acc
       
    
