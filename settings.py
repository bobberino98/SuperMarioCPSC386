class Settings:
    def __init__(self):
        self.brick_y_offset = 416  # Determines how low bricks appear on the screen
        self.color_mario_blue = (119, 108, 255)  # Classic blue background color
        self.game_title = "Super Mario"
        self.goomba_bottom = [23, 41, 52, 53, 98, 99, 115, 116, 125, 126, 129, 130, 200, 201]  # X offset of Goombas who spawn at groundlevel
        self.goomba_top = [81, 83]  # X offset of Goombas who spawn on platforms
        self.screen_height = 480
        self.screen_width = 1152

