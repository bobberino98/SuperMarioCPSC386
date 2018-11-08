from pygame.sprite import Sprite
from imagerect import ImageRect
from gravity import Gravity


class Enemy(Sprite):
    def __init__(self, screen, mario, settings, gamemap, enemy_type, x, y):
        super(Enemy, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.speed = 1
        self.mario = mario
        self.settings = settings
        self.enemy_type = enemy_type
        self.gamemap = gamemap
        if self.enemy_type == 'g':
            self.filename = "media/images/enemy/1"
            self.im_rect = ImageRect(screen, self.filename, 32, 32)
            self.rect = self.im_rect.rect
            self.rect.x = x
            self.rect.y = y

    def __str__(self):
        return "Enemy of type:" + self.enemy_type

    def update(self, delta):
        if self.rect.x - self.mario.rect.x < self.screen_rect.width and self.gamemap.object_hit_brick(self):
            self.rect.x -= self.speed*delta
        if self.gamemap.enemy_collide(self):
            self.speed *= -1
        elif not self.gamemap.object_hit_brick(self):
            Gravity.perform(self)
        self.im_rect.blitme()
