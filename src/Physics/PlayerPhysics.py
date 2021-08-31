
from Physics.PhysicsInterface import PhysicsInterface
from Physics.Velocity import Velocity
from TwoDim import TwoDim
from parameters import ACCELERATION, CELL_WIDTH, MAX_SPEED
from Physics.Acceleration import Acceleration
from Physics.Position import Position
class PlayerPhysics(PhysicsInterface):
    def __init__(self,pos=Position(), vel=Velocity(), acc=Acceleration()) -> None:
        super().__init__(pos=pos, vel=vel, acc=acc)
        self.last_direction = None
    def update_pos(self, scene):
        
        self.vel.calc_new_speed(self.acc)
      
       
        magnitude = self.vel.magnitude()

        if magnitude > MAX_SPEED:
            self.vel.x *= MAX_SPEED / magnitude
            self.vel.y *= MAX_SPEED / magnitude
        self.pos.calc_pos(self.vel.x, self.vel.y, scene)
        if self.acc.x != 0 or self.acc.y != 0:
            self.last_direction = self.acc.get_tuple()
        self.vel = Velocity()
        print(self.last_direction)
