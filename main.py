import arcade
from con import *


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__()
        self.bg = arcade.load_texture('bg.png')

    def setup(self):
        pass
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)



window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.run()
