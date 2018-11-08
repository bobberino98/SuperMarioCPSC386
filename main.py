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
        self.stats = Stats(settings)
        self.scoreboard = Scoreboard(settings, self.screen, self.stats)
        self.enemies = []
        goomba_bot = [23, 41, 52, 53, 98, 99, 115, 116, 125, 126, 129, 130, 200, 201]
        goomba_top = [81, 83]
        self.map = Map(self.screen, settings, self.enemies)
        self.mario = Mario(self.screen, settings, self.map)
        for x in goomba_bot:
            goomba = Enemy(self.screen, self.mario, settings, self.map, 'g', x * 32, settings.brick_y_offset - 32)
            self.enemies.append(goomba)
        for x in goomba_top:
            goomba = Enemy(self.screen, self.mario, settings, self.map, 'g', x * 32, settings.brick_y_offset - 8*32)
            self.enemies.append(goomba)

        self.bgm = pygame.mixer.Sound("media/sounds/bgm.wav")

    def __str__(self):
        return settings.game_title

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
                # for x in self.enemies:
                #   x.update(delta)
                pygame.display.flip()
                ticks += 1
                delta = 0
            clock.tick(60)


game = Game()
game.play()
