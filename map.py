from pygame.sprite import Group
import pygame
from brick import *


class Map:
    def __init__(self, screen, settings):
        super(Map, self).__init__()
        self.brick_count = 80  # number of bricks to initially render
        self.brick_columns = []
        self.settings = settings
        self.screen = screen
        self.dist = 0
        self.gapcols = [70, 71, 87, 88, 89, 156, 157]  # Gap columns
        self.b3cols = [21, 23, 25, 78, 80, 95, 101, 102, 119, 130, 131, 171, 172, 174]
        self.b7cols = [81, 82, 83, 84, 85, 86, 87, 88, 92, 93, 94, 122, 123, 124, 129, 132]
        self.q7cols = [23, 95, 110, 130, 131]
        self.q3cols = [17, 22, 24, 79, 107, 110, 113, 173]
        self.lpipe1cols = [29]
        self.rpipe1cols = [30]

        for num in range(224):  # Build each column
            self.add_column(num)

    def add_column(self, num):  # Create a new column of bricks
        if num in self.gapcols:
            pass
        else:
            new_column = Group()
            if len(self.brick_columns) == 0:
                x = 0
            else:
                x = 32 * num
            for i in range(2):
                brick_temp = Brick(self.screen)
                brick_temp.rect.x = x
                brick_temp.rect.y = self.settings.brick_y_offset + (32 * i)
                new_column.add(brick_temp)
                if num in self.b3cols:
                    brick_temp = BreakBrick(self.screen)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 96
                    new_column.add(brick_temp)
                if num in self.q3cols:
                    brick_temp = QBrick(self.screen)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 96
                    new_column.add(brick_temp)
                if num in self.q7cols:
                    brick_temp = QBrick(self.screen)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 32*7
                    new_column.add(brick_temp)
                if num in self.b7cols:
                    brick_temp = BreakBrick(self.screen)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 32 * 7
                    new_column.add(brick_temp)

            self.brick_columns.append(new_column)

    def update(self):  # Update and then blit
        self.blitme()

    def scroll(self, speed):
        self.dist += speed
        for column in self.brick_columns:  # Blit all bricks
            for brick in column:
                brick.im_rect.rect.x -= speed

    def blitme(self):  # Blit everything on the map
        for column in self.brick_columns:   # Blit all bricks
            for x in column:
                x.im_rect.blitme()

    def object_hit_brick(self, item):
        for column in self.brick_columns:
                for brick in column:
                    if pygame.sprite.collide_rect(item, brick):
                        if abs(brick.rect.top - item.rect.bottom) <= 10:
                            # print(item.__str__() + " is touching the ground")
                            return True, "Floor"
