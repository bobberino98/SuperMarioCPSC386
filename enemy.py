from pygame.sprite import Sprite
from imagerect import ImageRect
from gravity import Gravity


class Enemy(Sprite):
    def __init__(self, screen, mario, settings, map, en_type, x):
        super(Enemy, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.speed = 1
        self.mario = mario
        self.settings = settings
        self.map = map
        if en_type == 'g':
            self.filename = "media/images/enemy/goomba"
            self.im_rect = ImageRect(screen, self.filename, 32, 32)
            self.rect = self.im_rect.rect
            self.rect.x = x
            self.rect.y = self.settings.brick_y_offset - 32

    def update(self, delta):
        if self.rect.x - self.mario.rect.x < self.screen_rect.width and self.map.object_hit_brick(self):
            self.rect.x -= self.speed*delta
        if self.map.enemy_collide(self):
            self.speed *= -1
        elif not self.map.object_hit_brick(self):
            Gravity.perform(self)
        self.im_rect.blitme()
