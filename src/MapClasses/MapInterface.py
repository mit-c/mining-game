from typing import List
from Physics.Position import Position
from parameters import CELL_WIDTH


class MapInterface:
    def __init__(self, file_name="") -> None:
        if file_name:
            self.dict  = self.read_file(file_name)
        else:
            self.dict ={}
        self.file_name = file_name
        self.transformed_dict = {}
    def read_file(self,file_name):
        out_dict = {}
        with open(file_name, "r") as map:
            for j,line in enumerate(map):
                if line[0] == "%":
                    continue
                dict_to_update = {Position(i*CELL_WIDTH,j*CELL_WIDTH): char for i,char in enumerate(line) if not (char == '\n' or char == " ")}
                out_dict.update(dict_to_update)
        return out_dict
    
    def __repr__(self) -> str:
        with open(self.file_name, "r") as map:
            contents = map.read()
            return contents

    def transform_by_player_pos(self, pos):
        
        new_dict = {}
        for pos_entity in self.dict:

            new_dict[Position(pos_entity.x - pos.x, pos_entity.y - pos.y)] = self.dict[pos_entity]
        self.transformed_dict  = new_dict