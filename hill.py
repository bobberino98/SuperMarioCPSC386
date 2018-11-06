import pygame
from pygame.sprite import Sprite


class Hill(Sprite):
    def __init__(self, screen, size, scale_x, scale_y):
        super(Hill, self).__init__()
        self.screen = screen
        file = "media/images/hill/" + size + ".png"
        self.image = pygame.image.load(file)
        self.image = pygame.transform.scale(self.image, (scale_x, scale_y))
        self.rect = self.image.get_rect()

    def __str__(self):
        return 'Hill: x:' + str(self.rect.x) + ' Y:' + str(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
