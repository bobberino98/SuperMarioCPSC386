from pygame.sprite import Sprite
from imagerect import ImageRect


class Pipe(Sprite):
    def __init__(self, screen, num):
        super(Pipe, self).__init__()
        self.screen = screen
        self.type = "pipe"
        if num == 1:
            self.im_rect = ImageRect(screen, "media/images/pipe/pipe1", 64, 64)
        elif num == 2:
            self.im_rect = ImageRect(screen, "media/images/pipe/pipe2", 64, 96)
        elif num == 3:
            self.im_rect = ImageRect(screen, "media/images/pipe/pipe3", 64, 128)
        self.rect = self.im_rect.rect
