from PIL import Image
from random import randint,seed
import pygame as pyg

from parameters import CELL_WIDTH

class SpriteReader:
    def __init__(self) -> None:
        self.image_dict = {}
        self.load_rocks()
        self.load_background()

    def load_background(self):
        im = Image.open(r"src\sprites\tile.png")
        width, height = im.size
        adj_width, adj_height = width - CELL_WIDTH, height-CELL_WIDTH
        
        arr = []
        for _ in range(3):
            i= randint(0,adj_width)
            j=randint(0,adj_height)
            a,b,c,d = (i, j, i+CELL_WIDTH, (j+CELL_WIDTH))
            tile_PIL = im.crop((a,b,c,d))
            tile_PYG = self.convert_PIL_to_PYG(tile_PIL)
            arr.append(tile_PYG)
        self.image_dict["tiles"] = arr
    def load_rocks(self):

        im = Image.open(r"src\sprites\rocks.png")
        width, height = im.size
        step_w = width // 8
        step_h = height // 8
        rocks_PIL = [im.crop((i * step_w, j * step_h, (i+1) * step_w, (j+1) * step_h)).resize((CELL_WIDTH, CELL_WIDTH), Image.ANTIALIAS)
                 for i in range(8) for j in range(8)]

        rocks_PYG = [self.convert_PIL_to_PYG(rock_PIL) for rock_PIL in rocks_PIL]
        self.image_dict["rocks"] = rocks_PYG

    def convert_PIL_to_PYG(self,img_PIL):
        size = img_PIL.size
        mode = img_PIL.mode
        data = img_PIL.tobytes()
        img_PYG = pyg.image.fromstring(data,size,mode)
        return img_PYG

    def print(self) -> None:
        for key in self.image_dict:
            for im in self.image_dict[key]:
                im.show()

    def get_random(self, key):
        images = self.image_dict[key]
        num_img = len(images)
        rx = randint(0, num_img-1)
        return images[rx]

    def get_random_same_every_time(self, key, number):
        seed(1)
        out_imgs = []
        for i in range(number):
            images = self.image_dict[key]
            num_img = len(images)
            rx = randint(0, num_img-1)
            out_imgs.append(images[rx])
        return out_imgs

    def get_index(self, key, ix):
        images =self.image_dict[key]
        num_img = len(images)
        return images[ix % num_img]
        