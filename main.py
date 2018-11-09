import pygame
from settings import Settings
from user_control import Controller
from map import Map
from mario import Mario
from enemy import Enemy
from stats import Stats
from scoreboard import Scoreboard
settings = Settings()


class Game:
    def __init__(self):

        pygame.init()

        pygame.display.set_caption(settings.game_title)
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        self.stats = Stats()
        self.scoreboard = Scoreboard(settings, self.screen, self.stats)
        self.enemies = []

        self.map = Map(self.screen, settings, self.enemies)
        self.mario = Mario(self.screen, settings, self.map)
        for x in settings.goomba_bottom:
            goomba = Enemy(self.screen, self.mario, settings, self.map, 'g', x * 32, settings.brick_y_offset - 32)
            self.enemies.append(goomba)
        for x in settings.goomba_top:
            goomba = Enemy(self.screen, self.mario, settings, self.map, 'g', x * 32, settings.brick_y_offset - 8*32)
            self.enemies.append(goomba)

        self.bgm = pygame.mixer.Sound("media/sounds/bgm.wav")

    def __str__(self):
        return settings.game_title

    ''' Removes items from memory once they've gone offscreen. Helps save memory and improve efficiency.
    Currently only tested to work on lists containing objects of class Enemy'''
    @staticmethod
    def remove_unused_items(self, items):
        for item in items:
            if item.rect.right < 0:
                # print("Removing " + item.__str__() + " for being left of user game view")
                items.remove(item)
            if item.rect.top > self.screen.get_rect().bottom:
                # print("Removing " + item.__str__() + " for falling out of user game view")
                items.remove(item)

    def play(self):
        clock = pygame.time.Clock()
        self.bgm.play(-1)
        user_control = Controller(self.mario)
        time_per_tick = 1000 / 60
        delta = 0

        last_time = pygame.time.get_ticks()
        timer = 0
        ticks = 0
        while True:
            now = pygame.time.get_ticks()
            delta += (now-last_time)/time_per_tick
            timer += now-last_time
            last_time = now
            if delta >= 1:

                self.screen.fill(settings.color_mario_blue)
                user_control.check_events()
                self.map.update()
                self.scoreboard.prep_score()

                self.scoreboard.show_score()
                self.mario.update(self.map, delta)
                for x in self.enemies:
                    x.update(delta, self.mario, self.enemies)
                pygame.display.flip()
                ticks += 1
                delta = 0
            clock.tick(60)
            self.remove_unused_items(self, self.enemies)


game = Game()
game.play()
