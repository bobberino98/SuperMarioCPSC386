from pygame.sprite import Sprite
from gravity import Gravity
import pygame


class Enemy(Sprite):
    def __init__(self, screen, mario, settings, gamemap, enemy_type, x, y):
        super(Enemy, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.speed = -1
        self.mario = mario
        self.settings = settings
        self.enemy_type = enemy_type
        self.gamemap = gamemap
        self.last_img_update = pygame.time.get_ticks()
        self.last_img_mode = 1  # Used for character animation
        self.status = "Walking"  # Walking || Dying || Dead || DisplayingScore
        self.killed_time = None  # The time when the enemy made contact with (was killed by) Mario
        self.killed_delay_time = 300  # Ticks to wait before displaying the enemy's point value
        if self.enemy_type == 'g':
            img_string = "media/images/enemy/goomba/" + str(self.last_img_mode) + ".png"
            self.image = pygame.image.load(img_string)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def __str__(self):
        return "Enemy of type:" + self.enemy_type

    # Checks for collisions between Mario and enemies
    @staticmethod
    def check_collisions(mario, goombas, stats, settings):
        hit_goomba = pygame.sprite.spritecollideany(mario, goombas)
        if hit_goomba:
            if hit_goomba.status == "Walking":
                if mario.rect.bottom - hit_goomba.rect.top < 5:
                    stats.score += 100
                    hit_goomba.killed_time = pygame.time.get_ticks()
                    hit_goomba.status = "Dying"
                    hit_goomba.speed = 0
                if mario.rect.bottom - hit_goomba.rect.bottom <= 1 and hit_goomba.status == "Walking":  # Are Mario and the enemy next to eachother on the vertical (y) axis?
                    if hit_goomba.rect.left - mario.rect.right < 2:
                        # print("Mario collided with goombas left side")
                        settings.game_active = False
                        settings.game_status = "Reset"
                        stats.decrement_lives()
                    if mario.rect.left - hit_goomba.rect.right < 2:
                        # print("Mario collided with goombas right side")
                        settings.game_active = False
                        stats.decrement_lives()

    def update(self, mario, goombas, stats, settings):
        self.check_collisions(mario, goombas, stats, settings)

        if self.status == "Dying":
            if pygame.time.get_ticks() - self.killed_time > self.killed_delay_time:  # If enough time has passed since the enemy was killed
                self.status = "DisplayingScore"  # Show the enemy's point value

        if self.status == "DisplayingScore":
            self.rect.y -= 5
            if pygame.time.get_ticks() - self.killed_time > 1000:  # If enough time has passed since the score began displaying
                goombas.remove(self)  # Remove the score and the enemy simultaneously

        if self.gamemap.object_touching_wall(self):
            self.speed *= -1

        # Walking
        self.rect.x += 1 * self.speed

        # Perform gravity
        if not self.gamemap.object_touching_ground(self):
            Gravity.perform(self)

        self.animate()
        self.blitme()

    # Changes enemy's image to implement walking animation
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

    # Blit enemy
    def blitme(self):
        self.screen.blit(self.image, self.rect)
