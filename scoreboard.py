import pygame


class Scoreboard:

    def __init__(self, settings, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.template = pygame.image.load("media/images/other/scoreboard.png")
        self.template_rect = self.template.get_rect()

        self.score_image = self.settings.font_scoreboard.render(str(stats.score), True, self.settings.color_white, self.settings.color_mario_blue)
        self.score_rect = self.score_image.get_rect()

        self.coins_image = self.settings.font_scoreboard.render(str(stats.coins), True, self.settings.color_white, self.settings.color_mario_blue)
        self.coins_rect = self.coins_image.get_rect()

        self.time_image = self.settings.font_scoreboard.render(str(stats.time), True, self.settings.color_white, self.settings.color_mario_blue)
        self.time_rect = self.time_image.get_rect()

        self.life_image = self.settings.font_scoreboard.render(str(self.stats.lives_left), True, self.settings.color_white, self.settings.color_mario_blue)
        self.life_rect = self.life_image.get_rect()

        self.prep_score()

    def prep_score(self):
        self.score_image = self.settings.font_scoreboard.render(str(self.stats.score), True, self.settings.color_white, self.settings.color_mario_blue)
        self.score_rect.left = self.screen_rect.left + 55
        self.score_rect.top = 65

        self.coins_image = self.settings.font_scoreboard.render(str(self.stats.coins), True, self.settings.color_white, self.settings.color_mario_blue)
        self.coins_rect.left = self.screen_rect.left + 325
        self.coins_rect.top = 65

        self.time_image = self.settings.font_scoreboard.render(str(self.stats.time), True, self.settings.color_white, self.settings.color_mario_blue)
        self.time_rect.left = self.screen_rect.left + 760
        self.time_rect.top = 65

        self.life_image = self.settings.font_scoreboard.render(str(self.stats.lives_left), True, self.settings.color_white, self.settings.color_mario_blue)
        self.life_rect.right = self.screen_rect.right - 95
        self.life_rect.top = 65

    def show_score(self):
        self.screen.blit(self.template, self.screen_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.coins_image, self.coins_rect)
        self.screen.blit(self.time_image, self.time_rect)
        self.screen.blit(self.life_image, self.life_rect)
