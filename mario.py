from pygame.sprite import Sprite
from gravity import Gravity
import pygame
import audio


class Mario(Sprite):
    SPEED_CAP = 5
    ACCEL_FACTOR = 0.025
    DECEL_FACTOR = 0.25
    FALL_FACTOR = 0.20
    TURN_FACTOR = 0.3

    def __init__(self, screen, settings, gamemap):
        super(Mario, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.gravity = Gravity()
        self.gamemap = gamemap
        self.image = pygame.image.load("media/images/mario/standing.png")
        self.image = pygame.transform.scale(self.image, (35, 50))
        self.rect = self.image.get_rect()
        self.dist = 0
        self.speed = 0
        self.dir = 1  # -1 = moving left, 0 = standing still, 1 = moving right
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.jump_finished = False
        self.jump_speed = 0
        self.jump_start = False
        self.last_img_update = pygame.time.get_ticks()
        self.last_img_mode = 1

    def __str__(self):
        return 'Mario: x:' + str(self.rect.x) + ' y:' + str(self.rect.y)

    def update(self, gamemap, delta, stats):  # Update and then blit

        if self.rect.top > self.screen_rect.bottom + 80:  # Has Mario fallen offscreen?
            stats.decrement_lives()
            self.settings.game_active = False
            self.settings.game_status = "Reset"
            return

        if not self.jumping and not gamemap.object_hit_brick(self):
            self.gravity.perform(self)

        if self.jumping:
            if gamemap.object_hit_brick(self):
                audio.play(0)
            self.jump()
        elif self.jumping and gamemap.object_hit_brick(self):
            self.jump()
        elif self.gamemap.object_hit_brick:
            self.jump_start = False
            self.jump_speed = 0
        if self.moving_left:
            if self.dir == 1 and self.speed != 0:
                self.turn()
            elif self.dir == 0:
                self.dir = -1
            self.accelerate()
            if self.rect.x > 0:
                self.rect.x += self.dir * self.speed * delta

        elif self.moving_right:
            if self.dir == -1 and self.speed != 0:
                self.turn()
            elif self.dir == 0:
                self.dir = 1
            self.accelerate()
            if self.rect.centerx >= self.screen_rect.width/2:

                self.gamemap.scroll(self.speed)
            else:
                self.rect.x += self.dir * self.speed * delta
        else:
            self.decelerate()
            if self.rect.x > 0 and self.rect.right < self.screen_rect.width:
                self.rect.x += self.dir * self.speed * delta
            if self.rect.centerx >= self.screen_rect.width / 2:
                self.gamemap.scroll(self.speed)

        self.rect.y -= self.jump_speed*delta
        self.gamemap.collide(self)
        self.animate()
        self.blitme()

    def animate(self):
        if pygame.time.get_ticks() - self.last_img_update >= 50:
            if self.jumping:
                img_string = "media/images/mario/jumping_1.png"
                self.image = pygame.image.load(img_string)
                self.image = pygame.transform.scale(self.image, (35, 50))
                if self.dir == -1:
                    self.image = pygame.transform.flip(self.image, 1, 0)
            elif self.moving_right or self.moving_left:
                if self.gamemap.object_hit_brick:
                    img_string = "media/images/mario/walking_" + str(self.last_img_mode) + ".png"
                    self.image = pygame.image.load(img_string)
                    self.image = pygame.transform.scale(self.image, (35, 50))
                    if self.dir == -1:
                        self.image = pygame.transform.flip(self.image, 1, 0)

            else:
                img_string = "media/images/mario/standing.png"
                self.image = pygame.image.load(img_string)
                self.image = pygame.transform.scale(self.image, (35, 50))
                if self.dir == -1:
                    self.image = pygame.transform.flip(self.image, 1, 0)

            if self.last_img_mode == 4:
                self.last_img_mode = 1
            else:
                self.last_img_mode += 1
            self.last_img_update = pygame.time.get_ticks()

    def accelerate(self):
        if self.speed == 0:
            self.speed = 2 + Mario.ACCEL_FACTOR
        if self.speed < Mario.SPEED_CAP:
            self.speed *= 1 + Mario.ACCEL_FACTOR

    def decelerate(self):
        if self.speed >= Mario.ACCEL_FACTOR:
            self.speed -= Mario.DECEL_FACTOR
        else:
            self.speed = 0
            self.dir = 0

    def turn(self):
        if self.speed >= Mario.ACCEL_FACTOR:
            self.speed -= Mario.TURN_FACTOR
        else:
            self.speed = 0
            self.dir *= -1

    def jump(self):
        if not self.jump_finished:
            self.jump_start = True
            if self.jump_speed <= 0:
                self.jump_speed = 7
            else:
                self.jump_speed -= Mario.FALL_FACTOR
                if self.jump_speed <= 0:
                    self.jump_finished = True
                elif self.gamemap.object_hit_brick(self):
                    self.jump_finished = True

        else:
            self.jump_speed -= Mario.FALL_FACTOR
            if self.gamemap.object_hit_brick(self):
                self.jump_finished = False
                self.jump_start = False

    def blitme(self):  # Blit Mario
        self.screen.blit(self.image, self.rect)
