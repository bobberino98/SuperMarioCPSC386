import pygame
from settings import Settings
from user_control import Controller
from map import Map
from mario import Mario

settings = Settings()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.game_title)
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        self.map = Map(self.screen, settings)
        self.mario = Mario(self.screen, settings, self.map)

    def __str__(self):
        return settings.game_title

    def play(self):
        user_control = Controller(self.mario)
        while True:
            self.screen.fill(settings.color_mario_blue)
            user_control.check_events()
            self.map.update()
            self.mario.update(self.map)
            pygame.display.flip()


game = Game()
game.play()
