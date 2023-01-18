import time
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
            a=time.time()
            if (time.time()-a)>10:
                del self.snake
                del self.food1
                del self.food2
                del self.trap


        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake.move()
        
        if arcade.check_for_collision(self.snake,self.food1):
            self.snake.eat(self.food1, 1)
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


        



    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x=0
            self.snake.change_y=1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x=0
            self.snake.change_y=-1
        elif symbol == arcade.key.LEFT:
            self.snake.change_x=-1
            self.snake.change_y=0
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x=1
            self.snake.change_y=0
        


game=Game()
arcade.run()

        
