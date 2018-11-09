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
        self.status = "Walking"  # Walking || Dying || Dead || DisplayingScore
        self.killed_time = None  # The time when the enemy made contact with (was killed by) Mario
        self.killed_delay_time = 300
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
            if hit_goomba.status == "Walking":
                if mario.rect.bottom - hit_goomba.rect.top < 10:
                    hit_goomba.killed_time = pygame.time.get_ticks()
                    hit_goomba.status = "Dying"
                    hit_goomba.speed = 0

    def update(self, delta, mario, goombas):
        self.check_collisions(mario, goombas)

        if self.status == "Dying":
            # Show Goomba's point value
            if pygame.time.get_ticks() - self.killed_time > self.killed_delay_time:
                self.status = "DisplayingScore"

        if self.status == "DisplayingScore":
            # Show Goomba's point value
            self.rect.y -= 5
            if pygame.time.get_ticks() - self.killed_time > 1000:
                goombas.remove(self)

        # Walking left
        if self.rect.x - self.mario.rect.x < self.screen_rect.width and self.gamemap.object_hit_brick(self):
            self.rect.x -= self.speed*delta

        # Change direction on collision? Please clarify
        if self.gamemap.enemy_collide(self):
            self.speed *= -1

        # Gravity always on
        elif not self.gamemap.object_hit_brick(self):
            Gravity.perform(self)

        self.animate()
        self.blitme()

    '''Changes a Goombas image to emulate walking animation'''
    def animate(self):
        if pygame.time.get_ticks() - self.last_img_update >= 100:
            if self.status == "Walking":
                img_string = "media/images/enemy/goomba/" + str(self.last_img_mode) + ".png"
                self.image = pygame.image.load(img_string)
                self.image = pygame.transform.scale(self.image, (32, 32))
                if self.speed == -1:
                    self.image = pygame.transform.flip(self.image, 1, 0)
                if self.last_img_mode == 2:
                    self.last_img_mode = 1
                else:
                    self.last_img_mode += 1
            if self.status == "Dying":
                img_string = "media/images/enemy/goomba/" + str(3) + ".png"
                self.image = pygame.image.load(img_string)
                self.image = pygame.transform.scale(self.image, (32, 32))
                if self.speed == -1:
                    self.image = pygame.transform.flip(self.image, 1, 0)
                if self.last_img_mode == 4:
                    self.last_img_mode = 3
                else:
                    self.last_img_mode += 1
            if self.status == "DisplayingScore":
                img_string = "media/images/enemy/goomba/" + str(100) + ".png"
                self.image = pygame.image.load(img_string)
                self.image = pygame.transform.scale(self.image, (32, 32))
            self.last_img_update = pygame.time.get_ticks()

    def blitme(self):  # Blit enemy
        self.screen.blit(self.image, self.rect)
