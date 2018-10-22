import pygame
from settings import Settings

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))


class Game:
    def __init__(self):
        pygame.init()

    def play(self):
        pass


game = Game()
game.play()
