from MapClasses.MapInterface import MapInterface
from Physics.Position import Position
from parameters import CELL_WIDTH

# This class seems unecessary but inherits useful functions to keep map fixed while player moves


class BackgroundMap(MapInterface):
    def __init__(self, file_name="") -> None:
        super().__init__(file_name=file_name)
        