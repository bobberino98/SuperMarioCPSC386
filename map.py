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
        self.brick_columns = []
        self.clouds = []
        self.hills = []
        self.bushes = []
        self.enemies = enemies
        self.settings = settings
        self.screen = screen
        self.dist = 0
        self.mario = None
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

        self.flagpole = pygame.sprite.Sprite()
        self.flagpole.image = pygame.image.load("media/images/other/flagpole.png")
        self.flagpole.rect = self.flagpole.image.get_rect()
        self.flagpole.rect.x = 6420
        self.flagpole.rect.y = 142

        self.flag = pygame.sprite.Sprite()
        self.flag.image = pygame.image.load("media/images/other/flag.png")
        self.flag.rect = self.flag.image.get_rect()
        self.flag.rect.x = 6420
        self.flag.rect.y = 142

        self.castle = pygame.sprite.Sprite()
        self.castle.image = pygame.image.load("media/images/other/castle.png")
        self.castle.rect = self.castle.image.get_rect()
        self.castle.rect.x = 6515
        self.castle.rect.y = 282

        for num in range(224):  # Build each column
            self.add_column(num)

        self.add_clouds()
        self.add_hills()
        self.add_bushes()

    def set_mario(self, mario):
        self.mario = mario

    def mario_touching_flagpole(self):
        if pygame.sprite.collide_rect(self.mario, self.flagpole):
            self.settings.game_status = "Finishing"

    def mario_touching_castle(self):
        if pygame.sprite.collide_rect(self.mario, self.castle):
            return True
        else:
            return False

    def add_clouds(self):
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
        if num in self.gapcols:  # If this is a gap column (canyon)
            pass  # Do nothing
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
                    brick_temp = StairBrick(self.screen, 1)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 32
                    new_column.add(brick_temp)
                if num in self.stair2:
                    brick_temp = StairBrick(self.screen, 2)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 64
                    new_column.add(brick_temp)
                if num in self.stair3:
                    brick_temp = StairBrick(self.screen, 3)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 96
                    new_column.add(brick_temp)
                if num in self.stair4:
                    brick_temp = StairBrick(self.screen, 4)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 128
                    new_column.add(brick_temp)
                if num in self.stair5:
                    brick_temp = StairBrick(self.screen, 5)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 160
                    new_column.add(brick_temp)
                if num in self.stair6:
                    brick_temp = StairBrick(self.screen, 6)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 192
                    new_column.add(brick_temp)
                if num in self.stair7:
                    brick_temp = StairBrick(self.screen, 7)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 224
                    new_column.add(brick_temp)
                if num in self.stair8:
                    brick_temp = StairBrick(self.screen, 8)
                    brick_temp.rect.x = x
                    brick_temp.rect.y = self.settings.brick_y_offset - 256
                    new_column.add(brick_temp)
            self.brick_columns.append(new_column)

    def update(self):  # Update and then blit
        #if self
        self.mario_touching_flagpole()
        self.blitme()

    def scroll(self, speed):
        self.dist += speed
        for column in self.brick_columns:  # Move all brick columns
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
        self.flagpole.rect.x -= speed
        self.flag.rect.x -= speed
        self.castle.rect.x -= speed

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
        self.screen.blit(self.flagpole.image, self.flagpole.rect)
        self.screen.blit(self.flag.image, self.flag.rect)
        self.screen.blit(self.castle.image, self.castle.rect)

    # Called repeatedly by main once Mario has made contact with the flagpole
    def lower_flag(self):
        if self.flag.rect.y < 300:
            self.flag.rect.y += 1
            return "Lowering"
        else:
            return "Done"

    # Is a specified item toughing the ground?
    def object_touching_ground(self, item):
        for column in self.brick_columns:
                for brick in column:
                    if pygame.sprite.collide_rect(item, brick):
                        if abs(brick.rect.top - item.rect.bottom) <= 10:
                            return True
        return False

    # Is a specified item toughing a vertical rect edge
    def object_touching_wall(self, item):
        for column in self.brick_columns:
            for brick in column:
                if pygame.sprite.collide_rect(item, brick):
                        if abs(brick.rect.left - item.rect.right) <= 10:
                            if abs(brick.rect.top - item.rect.bottom) > 10:
                                return True
                        if abs(item.rect.left - brick.rect.right) <= 10:
                            if abs(brick.rect.top - item.rect.bottom) > 10:
                                return True
        return False

    def enemy_collide(self, item):
        for column in self.brick_columns:
                for brick in column:
                    if brick.type != "floor":
                        if pygame.sprite.collide_rect(item, brick):
                            return True

    def collide(self, item):
        for column in self.brick_columns:
                for brick in column:
                    if item.rect.bottom < self.settings.brick_y_offset - 192:
                        if brick.type != "stair_7":
                            if pygame.sprite.collide_rect(item, brick):
                                return self.collide_helper(item, brick)

                    elif item.rect.bottom < self.settings.brick_y_offset - 160:
                        if brick.type != "stair_6":
                            if pygame.sprite.collide_rect(item, brick):
                                return self.collide_helper(item, brick)

                    elif item.rect.bottom < self.settings.brick_y_offset - 128:
                        if brick.type != "stair_5":
                            if pygame.sprite.collide_rect(item, brick):
                                return self.collide_helper(item, brick)

                    elif item.rect.bottom < self.settings.brick_y_offset - 96:
                        if brick.type != "stair_4":
                            if pygame.sprite.collide_rect(item, brick):
                                return self.collide_helper(item, brick)

                    elif item.rect.bottom < self.settings.brick_y_offset - 64:
                        if brick.type != "stair_3":
                            if pygame.sprite.collide_rect(item, brick):
                                return self.collide_helper(item, brick)

                    elif item.rect.bottom < self.settings.brick_y_offset - 32:
                        if brick.type != "stair_2":
                            if pygame.sprite.collide_rect(item, brick):
                                return self.collide_helper(item, brick)

                    elif item.rect.bottom < self.settings.brick_y_offset:
                        if brick.type != "stair_1":
                            if pygame.sprite.collide_rect(item, brick):
                                return self.collide_helper(item, brick)

                    elif brick.type != "floor":
                        if pygame.sprite.collide_rect(item, brick):
                            return self.collide_helper(item, brick)

    @staticmethod
    def collide_helper(item, brick):
        if item.jump_speed > 0 and item.rect.bottom > brick.rect.bottom:
            item.rect.top = brick.rect.bottom
            item.speed = 0
        elif item.speed * item.dir > 0 and item.rect.centery > brick.rect.top:  # Reports if Mario has collided with a brick's left side
            item.rect.right = brick.rect.left
            item.decelerate()
            item.speed = 0
        elif item.speed * item.dir < 0 and item.rect.centery > brick.rect.top:  # Reports if Mario has collided with a brick's right side
            item.rect.left = brick.rect.right
            item.decelerate()
            item.speed = 0
        return True
