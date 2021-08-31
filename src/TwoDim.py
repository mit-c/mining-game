

class TwoDim:
    def __init__(self,x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.tuple = (x,y)


    def normalise_tuple(self):
        x,y = self.tuple
        if x == 0 and y == 0:
            self.tuple= (0,0)
            return
        norm = (x**2 + y**2) ** 0.5
        self.tuple = (x/norm, y/norm)

    def magnitude(self):
        norm = (self.x**2 + self.y**2) ** 0.5
        return norm

    def set_tuple(self):
        self.tuple = (self.x, self.y)
    
    def __repr__(self) -> str:
        return f"{self.x}, {self.y}"

    def get_tuple(self):
        return self.tuple