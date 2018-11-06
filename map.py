from pygame.sprite import Group
import pygame
from brick import *
from cloud import Cloud
from hill import Hill
from bush import Bush
from pipe import Pipe


class Map:
    def __init__(self, screen, settings, enemies):
        super(Map, self).__init__()
        self.brick_count = 80  # number of bricks to initially render
        self.brick_columns = []
        self.clouds = []
        self.hills = []
        self.bushes = []
        self.enemies = enemies
        self.settings = settings
        self.screen = screen
        self.dist = 0
        self.gapcols = [70, 71, 87, 88, 89, 156, 157]  # Gap columns
        self.b3cols = [21, 23, 25, 78, 80, 95, 101, 102, 119, 130, 131, 171, 172, 174]
        self.b7cols = [81, 82, 83, 84, 85, 86, 87, 88, 92, 93, 94, 122, 123, 124, 129, 132]
        self.q7cols = [23, 95, 110, 130, 131]
        self.q4cols = [17, 22, 24, 79, 107, 110, 113, 173]
        self.pipe1cols = [29, 182, 166]
        self.pipe2cols = [39]
        self.pipe3cols = [47, 57]
        self.stair1 = [137, 146, 151, 161, 184, 201]
        self.stair2 = [138, 145, 152, 160, 185]
        self.stair3 = [139, 144, 153, 159, 186]
        self.stair4 = [140, 143, 154, 155, 158, 187]
        self.stair5 = [188]
        self.stair6 = [189]
        self.stair7 = [190]
        self.stair8 = [191, 192]
        self.cloudS1 = [9, 57, 105, 153, 201]
        self.cloudS2 = [20, 68, 116, 164, 212]
        self.cloudM = [37, 85, 133, 181]
        self.cloudL = [28, 76, 124, 172]
        self.hillL = [1, 49, 97, 145, 193]
        self.hillS = [17, 65, 113, 161, 208]

        self.bushL = [12, 60, 108]
        self.bushM = [42, 90, 140]
        self.bushS = [24, 72, 120, 158, 168, 205, 215]

        for num in range(224):  # Build each column
            self.add_column(num)

        self.add_clouds()
        self.add_hills()
        self.add_bushes()

    def add_clouds(self):
        # TODO
        ''' This should be transformed into a loop such that
        all clouds are generated at once '''
        for x in self.cloudS1:
            small = Cloud(self.screen, "small", 64, 48)
            small.rect.x = x*32
            small.rect.y = 96
            self.clouds.append(small)
        for x in self.cloudS2:
            small = Cloud(self.screen, "small", 64, 48)
            small.rect.x = x * 32
            small.rect.y = 64
            self.clouds.append(small)
        for x in self.cloudM:
            small = Cloud(self.screen, "medium", 96, 48)
            small.rect.x = x*32
            small.rect.y = 64
            self.clouds.append(small)
        for x in self.cloudL:
            small = Cloud(self.screen, "large", 128, 48)
            small.rect.x = x*32
            small.rect.y = 96
            self.clouds.append(small)

    def add_hills(self):
        for x in self.hillS:
            hill = Hill(self.screen, "small", 96, 64)
            hill.rect.x = x*32
            hill.rect.y = self.settings.brick_y_offset - 64
            self.hills.append(hill)
        for x in self.hillL:
            hill = Hill(self.screen, "large", 160, 96)
            hill.rect.x = x*32
            hill.rect.y = self.settings.brick_y_offset - 96
            self.hills.append(hill)

    def add_bushes(self):
        for x in self.bushS:
            bush = Bush(self.screen, "small", 96, 32)
            bush.rect.x = x * 32
            bush.rect.y = self.settings.brick_y_offset - 32
            self.bushes.append(bush)
        for x in self.bushM:
            bush = Bush(self.screen, "medium", 128, 32)
            bush.rect.x = x * 32
            bush.rect.y = self.settings.brick_y_offset - 32
            self.bushes.append(bush)
        for x in self.bushL:
            bush = Bush(self.screen, "large", 160, 32)
            bush.rect.x = x * 32
            bush.rect.y = self.settings.brick_y_offset - 32
            self.bushes.append(bush)

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
                    brick_temp.rect.y = self.settings.brick_y_offset - 128
                    new_column.add(brick_temp)
                if num in self.q4cols:
                    brick_temp = QBrick(self.screen)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 128
                    new_column.add(brick_temp)
                if num in self.q7cols:
                    brick_temp = QBrick(self.screen)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 32 * 7
                    new_column.add(brick_temp)
                if num in self.b7cols:
                    brick_temp = BreakBrick(self.screen)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 32 * 7
                    new_column.add(brick_temp)
                if num in self.pipe3cols:
                    brick_temp = Pipe(self.screen, 3)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 128
                    new_column.add(brick_temp)
                if num in self.pipe1cols:
                    brick_temp = Pipe(self.screen, 1)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 64
                    new_column.add(brick_temp)
                if num in self.pipe2cols:
                    brick_temp = Pipe(self.screen, 2)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 96
                    new_column.add(brick_temp)
                if num in self.pipe3cols:
                    brick_temp = Pipe(self.screen, 3)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 128
                    new_column.add(brick_temp)
                if num in self.stair1:
                    brick_temp = StairBrick(self.screen)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 32
                    new_column.add(brick_temp)
                if num in self.stair2:
                    for n in range(2):
                        brick_temp = StairBrick(self.screen)
                        brick_temp.rect.x = x
                        brick_temp.rect.y = self.settings.brick_y_offset - (n+1)*32
                        new_column.add(brick_temp)
                if num in self.stair3:
                    for n in range(3):
                        brick_temp = StairBrick(self.screen)
                        brick_temp.rect.x = x
                        brick_temp.rect.y = self.settings.brick_y_offset - (n+1)*32
                        new_column.add(brick_temp)
                if num in self.stair4:
                    for n in range(4):
                        brick_temp = StairBrick(self.screen)
                        brick_temp.rect.x = x
                        brick_temp.rect.y = self.settings.brick_y_offset - (n+1)*32
                        new_column.add(brick_temp)
                if num in self.stair5:
                    for n in range(5):
                        brick_temp = StairBrick(self.screen)
                        brick_temp.rect.x = x
                        brick_temp.rect.y = self.settings.brick_y_offset - (n+1)*32
                        new_column.add(brick_temp)
                if num in self.stair6:
                    for n in range(6):
                        brick_temp = StairBrick(self.screen)
                        brick_temp.rect.x = x
                        brick_temp.rect.y = self.settings.brick_y_offset - (n+1)*32
                        new_column.add(brick_temp)
                if num in self.stair7:
                    for n in range(7):
                        brick_temp = StairBrick(self.screen)
                        brick_temp.rect.x = x
                        brick_temp.rect.y = self.settings.brick_y_offset - (n+1)*32
                        new_column.add(brick_temp)
                if num in self.stair8:
                    for n in range(8):
                        brick_temp = StairBrick(self.screen)
                        brick_temp.rect.x = x
                        brick_temp.rect.y = self.settings.brick_y_offset - (n+1)*32
                        new_column.add(brick_temp)

            self.brick_columns.append(new_column)

    def update(self):  # Update and then blit
        self.blitme()

    def scroll(self, speed):
        self.dist += speed
        for column in self.brick_columns:  # Blit all bricks
            for brick in column:
                brick.im_rect.rect.x -= speed
        for cloud in self.clouds:
            cloud.rect.x -= speed
        for hill in self.hills:
            hill.rect.x -= speed
        for bush in self.bushes:
            bush.rect.x -= speed
        for enemy in self.enemies:
            enemy.rect.x -= speed

    def blitme(self):  # Blit everything on the map
        for cloud in self.clouds:
            cloud.blitme()
        for hill in self.hills:
            hill.blitme()
        for bush in self.bushes:
            bush.blitme()
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

    def left_collide(self, item):
        for column in self.brick_columns:
                for brick in column:
                    if brick.type != "floor":
                        if pygame.sprite.collide_rect(item, brick) and item.rect.bottom > brick.rect.top + 1:
                            if abs(brick.rect.left - item.rect.right) <= 10:
                                # print(item.__str__() + " is touching the ground")
                                return True, "Left"

    def right_collide(self, item):
        for column in self.brick_columns:
                for brick in column:
                    if brick.type != "floor":
                        if pygame.sprite.collide_rect(item, brick):
                            if abs(brick.rect.right - item.rect.left) <= 10 and item.rect.bottom > brick.rect.top + 1:
                                # print(item.__str__() + " is touching the ground")
                                return True, "Right"
