import pygame
from settings import Settings
import user_control

settings = Settings()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.game_title)
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    def __str__(self):
        return settings.game_title

    def play(self):
        while True:
            self.screen.fill(settings.game_color)
            user_control.check_events()
            pygame.display.flip()


game = Game()
game.play()
