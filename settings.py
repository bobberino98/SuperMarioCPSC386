import pygame
import pygame.font


class Settings:
    def __init__(self):
        self.brick_y_offset = 416  # Determines how low bricks appear on the screen
        self.color_mario_blue = (119, 108, 255)  # Classic blue background color
        self.color_white = (255, 255, 255)  # Plain white
        self.font_scoreboard = pygame.font.SysFont(None, 88)
        self.game_active = True
        # game_status
        #   Ready - Normal state while game is being played
        #   Reset - Mario has died or some other event has happened, the map will be rebuilt and stats will reset
        #   Finishing - Mario has made contact with the flagpole and completed the level
        self.game_status = "Ready"
        self.game_title = "Super Mario"
        self.goomba_bottom = [23, 41, 52, 53, 98, 99, 115, 116, 125, 126, 129, 130, 200, 201]  # X offset of Goombas who spawn at groundlevel
        self.goomba_top = [81, 83]  # X offset of Goombas who spawn on platforms
        self.muted = False  # Background music muted status
        self.screen_height = 480
        self.screen_width = 1152
