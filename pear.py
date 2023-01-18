import random
import arcade
from fruit import Fruit


class Pear(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width=34
        self.height=34
        self.center_x=random.randint(17,game.width-17)
        self.center_y=random.randint(17,game.height-17)
        self.pic=arcade.load_texture("pear.png")

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x,self.center_y,self.width,self.height,self.pic)




