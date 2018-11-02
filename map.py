from pygame.sprite import Group
import pygame
import brick


class Map:
    def __init__(self, screen, settings):
        super(Map, self).__init__()
        self.brick_count = 80  # number of bricks to initially render
        self.brick_columns = []
        self.settings = settings
        self.screen = screen
        self.dist = 0
        for num in range(39):  # start with 18 columns of bricks
            self.add_column(num)

    def add_column(self, num):  # create a new column of bricks
        new_column = Group()
        if len(self.brick_columns) == 0:
            x = 0
        else:
            x = 32 * len(self.brick_columns)
        for i in range(2):
            brick_temp = brick.Brick(self.screen)
            brick_temp.rect.x = x
            brick_temp.rect.y = self.settings.brick_y_offset + (32 * i)
            new_column.add(brick_temp)
            if num == 17:
                brick_temp = brick.QBrick(self.screen)
                brick_temp.rect.x = x
                brick_temp.rect.y = self.settings.brick_y_offset - 96
                new_column.add(brick_temp)

        self.brick_columns.append(new_column)

    def update(self):  # Update and then blit
        self.blitme()

    def scroll(self, speed):
        self.dist += speed
        for column in self.brick_columns:   # Blit all bricks
            for brick in column:
                brick.im_rect.rect.x -= speed

    def blitme(self):   # Blit everything on the map
        for column in self.brick_columns:   # Blit all bricks
            for brick in column:
                brick.im_rect.blitme()

    def object_hit_ground(self, item):
        for x in self.brick_columns:
            if pygame.sprite.spritecollideany(item, x):
                # print(item.__str__() + " is touching the ground")
                return True
