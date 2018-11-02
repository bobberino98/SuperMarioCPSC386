import pygame
from pygame.sprite import Sprite
from imagerect import ImageRect


class Brick(Sprite):
    def __init__(self, screen):
        super(Brick, self).__init__()
        self.screen = screen
        self.im_rect = ImageRect(screen, "media/images/brick", 32, 32)
        self.rect = self.im_rect.rect

    def __str__(self):
        return 'Brick: x:' + str(self.rect.x) + ' y:' + str(self.rect.y)
