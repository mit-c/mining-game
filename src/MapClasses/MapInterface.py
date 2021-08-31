from typing import List


class MapInterface:
    def __init__(self, file_name) -> None:
        self.array: List[List[str]]  = self.read_file(file_name)
        self.file_name = file_name
    def read_file(self,file_name) -> List[List[str]]:
        out_arr = []
        with open(file_name, "r") as map:
            for line in map:
                if line[0] == "%":
                    continue
                list_to_add = [char for char in line]
                out_arr.append(list_to_add)
        return out_arr
    
    def __repr__(self) -> str:
        with open(self.file_name, "r") as map:
            contents = map.read()
            return contents

    
