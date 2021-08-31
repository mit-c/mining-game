from Physics.PlayerPhysics import PlayerPhysics
from parameters import DT, HEIGHT, WIDTH, MAP_WIDTH, MAP_HEIGHT

class Scene:
    def __init__(self, entities, player) -> None:
        self.entities = entities
        self.player_physics = player
        self.border = (HEIGHT, WIDTH)
    
    def collision_detection(self,current_pos, vel_x, vel_y):
        pos_x = current_pos.x + vel_x * DT
        pos_y = current_pos.y + vel_y * DT
        out_of_bounds_x = pos_x < -MAP_WIDTH or pos_x > MAP_WIDTH
        out_of_bounds_y = pos_y < -MAP_HEIGHT or pos_y > MAP_HEIGHT
    
        if out_of_bounds_x:
            pos_x = current_pos.x - vel_x * DT
        if out_of_bounds_y:
            pos_y = current_pos.y - vel_y * DT

        return pos_x, pos_y

