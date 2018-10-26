import pygame


class Map:
    def __init__(self, screen, settings):
        self.brick_count = 80  # number of bricks to initially render
        self.settings = settings
        self.screen = screen

    def blitme(self):
        image = pygame.image.load("media/images/brick.png")
        x = -75  # starting brick x offset
        y = self.settings.brick_y_offset
        for i in range(self.brick_count):
            self.screen.blit(image, (x, y))
            if i % 4 == 0:  # if we've reached the bottom of a column
                x += 75  # increment x offset
                y = self.settings.brick_y_offset  # reset y offset
            else:  # otherwise just increment y offset
                y += 75