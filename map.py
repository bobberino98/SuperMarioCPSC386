from pygame.sprite import Group
import pygame
from brick import Brick


class Map:
    def __init__(self, screen, settings):
        super(Map, self).__init__()
        self.brick_count = 80  # number of bricks to initially render
        self.brick_columns = []
        self.settings = settings
        self.screen = screen
        for x in range(36):  # start with 18 columns of bricks
            self.add_column()

    def add_column(self):  # create a new column of bricks
        new_column = Group()
        if len(self.brick_columns) == 0:
            x = 0
        else:
            x = 32 * len(self.brick_columns)
        for i in range(4):
            brick = Brick(self.screen)
            brick.rect.x = x
            brick.rect.y = self.settings.brick_y_offset + (32 * i)
            new_column.add(brick)
        self.brick_columns.append(new_column)

    def update(self):  # Update and then blit
        self.blitme()

    def blitme(self):   # Blit everything on the map
        for column in self.brick_columns:   # Blit all bricks
            for brick in column:
                brick.im_rect.blitme()

    def object_hit_ground(self, item):
        for x in self.brick_columns:
            if pygame.sprite.spritecollideany(item, x):
                # print(item.__str__() + " is touching the ground")
                return True
