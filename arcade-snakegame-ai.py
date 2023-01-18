import random
import arcade

from apple import Apple
from pear import Pear
from mushroom import Mushroom
from snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)
        self.snake=Snake(self)

        self.food1=Apple(self)
        self.food2=Pear(self)
        self.trap=Mushroom(self)

        self.game_status="run"


    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.food1.draw()
        self.food2.draw()
        self.trap.draw()

        arcade.draw_text(f"Score: {self.snake.score}", 8*self.width//10, 20 , arcade.color.WHITE  , bold=True)

        if self.game_status=="Game Over":
            arcade.draw_lrtb_rectangle_filled(0,self.width,self.height,0,arcade.color.BLACK)
            arcade.draw_text("GAME OVER!", self.width//5 , self.height//2 , arcade.color.RED , 30)

        arcade.finish_render()

    def on_update(self, delta_time: float):

        dx=self.snake.center_x - self.food1.center_x
        dy=self.snake.center_y - self.food1.center_y

        dx2=self.snake.center_x - self.food2.center_x
        dy2=self.snake.center_y - self.food2.center_y

        if (abs(dx)<abs(dx2)) and (abs(dy)<abs(dy2)) :
            
            if dx>0:
                if dy>0:
                    self.snake.change_x=-1
                    self.snake.change_y=-1
                elif dy<0:
                    self.snake.change_x=-1
                    self.snake.change_y=1
                else:
                    self.snake.change_x=-1
                    self.snake.change_y=0

            if dx<0:
                if dy>0:
                    self.snake.change_x=1
                    self.snake.change_y=-1
                elif dy<0:
                    self.snake.change_x=1
                    self.snake.change_y=1
                else:
                    self.snake.change_x=1
                    self.snake.change_y=0   

            if dx==0:
                if dy>0:
                    self.snake.change_x=0
                    self.snake.change_y=-1
                elif dy<0:
                    self.snake.change_x=0
                    self.snake.change_y=1
                else:
                    self.snake.change_x=0
                    self.snake.change_y=0    
        else:   
            if dx2>0:
                if dy2>0:
                    self.snake.change_x=-1
                    self.snake.change_y=-1
                elif dy2<0:
                    self.snake.change_x=-1
                    self.snake.change_y=1
                else:
                    self.snake.change_x=-1
                    self.snake.change_y=0

            if dx2<0:
                if dy2>0:
                    self.snake.change_x=1
                    self.snake.change_y=-1
                elif dy2<0:
                    self.snake.change_x=1
                    self.snake.change_y=1
                else:
                    self.snake.change_x=1
                    self.snake.change_y=0   

            if dx2==0:
                if dy2>0:
                    self.snake.change_x=0
                    self.snake.change_y=-1
                elif dy2<0:
                    self.snake.change_x=0
                    self.snake.change_y=1
                else:
                    self.snake.change_x=0
                    self.snake.change_y=0    



        self.snake.move()

        if arcade.check_for_collision(self.snake,self.food1):
            self.snake.eat(self.food1,1)
            self.food1=Apple(self)

        if arcade.check_for_collision(self.snake,self.food2):
            self.snake.eat(self.food2, 2)
            self.food2=Pear(self)

        if arcade.check_for_collision(self.snake,self.trap):
            self.snake.hit(self.trap)
            self.trap=Mushroom(self)
            if self.snake.score == 0 :
                self.game_status="Game Over"

        self.snake.check_pass_limits(self)



game=Game()
arcade.run()