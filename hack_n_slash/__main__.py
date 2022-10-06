import random

import arcade
from constants import ScreenConstants


class FlyingSprite(arcade.Sprite):
    def update(self):
        super().update()

        if self.bottom < -20:
            self.remove_from_sprite_lists()


class Start(arcade.Window):
    def __init__(self):
        super().__init__(
            ScreenConstants.WIDTH,
            ScreenConstants.HEIGHT,
            ScreenConstants.TITLE,
            resizable=True
        )

        self.paused: bool | None = None

        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.SAND)
        self.player = arcade.Sprite(
            "images/jet.png",
            center_x=self.width / 2,
            scale=0.1
        )
        self.paused = False
        self.player.bottom = 50
        self.all_sprites.append(self.player)

        arcade.schedule(self.add_enemy, 0.25)
        # arcade.schedule(self.add_cloud, 1)

    def add_enemy(self, delta_time: float):
        enemy = FlyingSprite("images/missile.png", flipped_vertically=True, scale=0.05)
        enemy.bottom = ScreenConstants.HEIGHT
        enemy.left = random.randint(0, self.width)
        enemy.velocity = (0, random.randint(-10, -5))

        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()

    def on_update(self, delta_time: float):
        if self.paused:
            return

        self.all_sprites.update()

        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

        if self.player.collides_with_list(self.enemies_list):
            arcade.close_window()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.W:
            self.player.change_y = 5

        if symbol == arcade.key.S:
            self.player.change_y = -5

        if symbol == arcade.key.A:
            self.player.change_x = -5

        if symbol == arcade.key.D:
            self.player.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.player.change_y = 0

        if symbol == arcade.key.S or symbol == arcade.key.A:
            self.player.change_x = 0


def setup():
    window = Start()

    arcade.run()


if __name__ == '__main__':
    setup()
