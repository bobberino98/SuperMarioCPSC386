import pygame
from pygame.sprite import Sprite


class Brick(Sprite):
    def __init__(self, screen):
        super(Brick, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("media/images/brick.png")
        self.rect = self.image.get_rect()

    def __str__(self):
        return 'Brick: x:' + str(self.rect.x) + ' y:' + str(self.rect.y)
