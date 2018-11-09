from pygame.sprite import Sprite
from gravity import Gravity
import pygame


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
        self.last_img_update = pygame.time.get_ticks()
        self.last_img_mode = 1
        self.walking = False
        if self.enemy_type == 'g':
            img_string = "media/images/enemy/goomba/" + str(self.last_img_mode) + ".png"
            self.image = pygame.image.load(img_string)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def __str__(self):
        return "Enemy of type:" + self.enemy_type

    @staticmethod
    def check_collisions(mario, goombas):
        hit_goomba = pygame.sprite.spritecollideany(mario, goombas)
        if hit_goomba:
            goombas.remove(hit_goomba)

    def update(self, delta, mario, goombas):
        self.check_collisions(mario, goombas)

        # Walking left
        if self.rect.x - self.mario.rect.x < self.screen_rect.width and self.gamemap.object_hit_brick(self):
            self.rect.x -= self.speed*delta
            self.walking = True
        else:
            self.walking = False

        # Change direction on collision? Please clarify
        if self.gamemap.enemy_collide(self):
            self.speed *= -1

        # Gravity always on
        elif not self.gamemap.object_hit_brick(self):
            Gravity.perform(self)

        self.animate()
        self.blitme()

    def animate(self):
        if pygame.time.get_ticks() - self.last_img_update >= 100:
            if self.walking:
                img_string = "media/images/enemy/goomba/" + str(self.last_img_mode) + ".png"
                self.image = pygame.image.load(img_string)
                self.image = pygame.transform.scale(self.image, (32, 32))
                if self.speed == -1:
                    self.image = pygame.transform.flip(self.image, 1, 0)
            if self.last_img_mode == 2:
                self.last_img_mode = 1
            else:
                self.last_img_mode += 1
            self.last_img_update = pygame.time.get_ticks()

    def blitme(self):  # Blit enemy
        self.screen.blit(self.image, self.rect)
