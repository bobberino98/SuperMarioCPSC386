from pygame.sprite import Sprite
from imagerect import ImageRect


class Brick(Sprite):  # Floor bricks
    def __init__(self, screen):
        super(Brick, self).__init__()
        self.screen = screen
        self.type = "floor"
        self.im_rect = ImageRect(screen, "media/images/brick/floor", 32, 32)
        self.rect = self.im_rect.rect

    def __str__(self):
        return 'Brick: x:' + str(self.rect.x) + ' y:' + str(self.rect.y)


class QBrick(Sprite):  # Question mark bricks
    def __init__(self, screen):
        super(QBrick, self).__init__()
        self.screen = screen
        self.type = "question"
        self.im_rect = ImageRect(screen, "media/images/brick/question", 32, 32)

        self.rect = self.im_rect.rect


class BreakBrick(Sprite):  # Floating bricks
    def __init__(self, screen):
        super(BreakBrick, self).__init__()
        self.screen = screen
        self.type = "breakable"
        self.im_rect = ImageRect(screen, "media/images/brick/platform", 32, 32)

        self.rect = self.im_rect.rect


class StairBrick(Sprite):
    def __init__(self, screen, num):
        super(StairBrick, self).__init__()
        self.screen = screen
        self.im_rect = ImageRect(screen, "media/images/brick/stair_brick_"+str(num), 32, 32*num)
        self.type = "stair_"+str(num)
        self.rect = self.im_rect.rect

