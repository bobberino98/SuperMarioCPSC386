import pygame
from pygame.sprite import Sprite


class Cloud(Sprite):
    def __init__(self, screen, size, scale_x, scale_y):
        super(Cloud, self).__init__()
        self.screen = screen
        file = "media/images/cloud/" + size + ".png"
        self.image = pygame.image.load(file)
        self.image = pygame.transform.scale(self.image, (scale_x, scale_y))
        self.rect = self.image.get_rect()

    def __str__(self):
        return 'Cloud: x:' + str(self.rect.x) + ' Y:' + str(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)