import arcade
from con import *


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__()
        self.bg = arcade.load_texture('bgs/main-bg.png')
        self.X_place = False
        self.O_place = False

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2 + 50, SCREEN_WIDTH + 300, SCREEN_HEIGHT + 100, self.bg)
        if self.X_place:
            arcade.draw_text('X', 125, 480, (255, 255, 255), 50)
        if self.O_place:
            arcade.draw_text('O', 385, 480, (255, 255, 255), 50)


    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.E:
            self.X_place = True
        if key == arcade.key.R:
            self.O_place = True


    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print(x, y)

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.run()
