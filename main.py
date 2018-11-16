import pygame
from settings import Settings
from user_control import Controller
from map import Map
from mario import Mario
from enemy import Enemy
from stats import Stats
from scoreboard import Scoreboard

pygame.init()
settings = Settings()


class Game:
    def __init__(self):
        pygame.display.set_caption(settings.game_title)
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        self.stats = Stats()
        self.scoreboard = Scoreboard(settings, self.screen, self.stats)
        self.enemies = []
        self.map = Map(self.screen, settings, self.enemies)
        self.mario = Mario(self.screen, settings, self.map)
        self.reset_enemies()
        self.bgm = pygame.mixer.Sound("media/sounds/bgm.wav")

    def __str__(self):
        return settings.game_title

    # Removes items from memory once they've gone offscreen. Helps save memory and improve efficiency.
    # Currently only tested to work on lists containing objects of class Enemy
    @staticmethod
    def remove_unused_items(self, items):
        for item in items:
            if item.rect.right < 0:
                # print("Removing " + item.__str__() + " for being left of user game view")
                items.remove(item)
            if item.rect.top > self.screen.get_rect().bottom:
                # print("Removing " + item.__str__() + " for falling out of user game view")
                items.remove(item)

    '''Clears the enemies list and rebuilds it from scratch'''
    def reset_enemies(self):
        self.enemies.clear()
        for x in settings.goomba_bottom:
            goomba = Enemy(self.screen, self.mario, settings, self.map, 'g', x * 32, settings.brick_y_offset - 32)
            self.enemies.append(goomba)
        for x in settings.goomba_top:
            goomba = Enemy(self.screen, self.mario, settings, self.map, 'g', x * 32, settings.brick_y_offset - 8*32)
            self.enemies.append(goomba)

    def play(self):
        clock = pygame.time.Clock()
        self.bgm.play(-1)
        user_control = Controller(self.mario, settings)
        time_per_tick = 1000 / 60
        delta = 0

        last_time = pygame.time.get_ticks()
        timer = 0
        ticks = 0
        while settings.game_active and settings.game_status == "Ready":
            if settings.muted:
                self.bgm.set_volume(0)
            else:
                self.bgm.set_volume(1)
            now = pygame.time.get_ticks()
            delta += (now-last_time)/time_per_tick
            timer += now-last_time
            last_time = now
            if delta >= 1:  # Please explain

                self.screen.fill(settings.color_mario_blue)
                user_control.check_events()
                self.map.update()
                self.scoreboard.prep_score()

                self.scoreboard.show_score()
                self.mario.update(self.map, delta, self.stats)
                for x in self.enemies:
                    x.update(delta, self.mario, self.enemies, self.stats, settings)
                pygame.display.flip()
                ticks += 1
                delta = 0
            clock.tick(60)
            self.stats.update()
            self.check_stats()
            self.remove_unused_items(self, self.enemies)
            if settings.game_status == "Reset":
                self.reset_game()

    def check_stats(self):
        if self.stats.lives_left == 0:
            settings.game_active = False
        if self.stats.time == 0:
            settings.game_active = False

    def reset_game(self):
        # print("Received reset request")
        self.bgm.stop()
        # Hard or soft?
        if self.stats.lives_left == 0:
            reset_type = "Hard"
            # print("Reset - Hard")
        else:
            reset_type = "Soft"
            # print("Reset - Soft")

        # Soft - Lives remain
        #   Only score and time are refreshed
        if reset_type == "Soft":
            self.stats.score = 0
            self.stats.time = 400
            self.stats.last_time_update = pygame.time.get_ticks()
            self.reset_enemies()
            self.map = Map(self.screen, settings, self.enemies)
            self.mario = Mario(self.screen, settings, self.map)

        # Hard -  All lives are gone
        #   All but high score are reset
        elif reset_type == "Hard":
            self.stats.score = 0
            self.stats.time = 400
            self.stats.last_time_update = pygame.time.get_ticks()
            self.stats.coins = 0
            self.stats.lives_left = 3
            self.reset_enemies()
            self.map = Map(self.screen, settings, self.enemies)
            self.mario = Mario(self.screen, settings, self.map)

        # The game has been reset, resume gameplay
        settings.game_status = "Ready"
        settings.game_active = True
        self.play()


game = Game()
game.play()
