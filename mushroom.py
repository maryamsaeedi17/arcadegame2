import random
import arcade
from fruit import Fruit


class Mushroom(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width=34
        self.height=28
        self.center_x=random.randint(17,game.width-17)
        self.center_y=random.randint(14,game.height-14)
        self.pic=arcade.load_texture("mushroom.png")
        

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x,self.center_y,self.width,self.height,self.pic)




