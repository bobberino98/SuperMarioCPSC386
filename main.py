import pygame
from settings import Settings
from user_control import Controller
from map import Map
from mario import Mario
from enemy import Enemy

settings = Settings()


class Game:
    def __init__(self):

        pygame.init()

        pygame.display.set_caption(settings.game_title)
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

        self.enemies = []
        goomba_bot = [23, 41, 52, 53, 98, 99, 115, 116, 125, 126, 129, 130, 200, 201]
        goomba_top = [81, 83]
        self.map = Map(self.screen, settings)
        self.mario = Mario(self.screen, settings, self.map)
        for x in goomba_bot:
            goomba = Enemy(self.screen, self.mario, settings, self.map, 'g', x * 32)
            self.enemies.append(goomba)

        # self.background = ImageRect(self.screen, "media/background", settings.screen_width, settings.screen_height)
        # self.background.rect.left = 0
        # self.background.rect.top = 0

        self.bgm = pygame.mixer.Sound("media/sounds/bgm.wav")

    def __str__(self):
        return settings.game_title

    def play(self):
        clock = pygame.time.Clock()
        # self.bgm.play(-1)
        user_control = Controller(self.mario)
        while True:
            self.screen.fill(settings.color_mario_blue)
            # self.background.blitme()
            user_control.check_events()
            self.map.update()
            self.mario.update(self.map)
            for x in self.enemies:
                x.update()
            pygame.display.flip()
            clock.tick(60)


game = Game()
game.play()
