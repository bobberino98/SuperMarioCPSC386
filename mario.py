import pygame
from pygame.sprite import Sprite
from gravity import Gravity


class Mario(Sprite):
    SPEED_CAP = 50
    ACCEl_FACTOR = 5
    def __init__(self, screen, settings):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.gravity = Gravity()
        self.image = pygame.image.load("media/images/mario/regular.png")
        self.rect = self.image.get_rect()
        self.direction = None

    def __str__(self):
        return 'Mario: x:' + str(self.rect.x) + ' y:' + str(self.rect.y)

    def update(self, gamemap):  # Update and then blit
        if not gamemap.object_hit_ground(self):
            self.gravity.perform(self)
        if self.direction == "LEFT":
            self.rect.x -= 1 * 5
            # self.direction = None
        elif self.direction == "RIGHT":
            self.rect.x += 1 * 5
            # self.direction = None
        self.direction = None
        self.blitme()

    def blitme(self):   # Blit Mario
        self.screen.blit(self.image, self.rect)
