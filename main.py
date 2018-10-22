import pygame
from settings import Settings

settings = Settings()
pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption(settings.game_title)


class Game:
    def __init__(self):
        pygame.init()

    def __str__(self):
        return settings.game_title

    def play(self):
        while settings.game_title:
            pygame.display.flip()


game = Game()
game.play()
