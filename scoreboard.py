import pygame.font


class Scoreboard:

    def __init__(self, settings, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 88)

        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.color_mario_blue)

        self.score_rect = self.score_image.get_rect()
        self.life_image = self.font.render(str(self.stats.lives_left), True, self.text_color,
                                           self.settings.color_mario_blue)

        self.life_rect = self.life_image.get_rect()
        self.prep_score()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.color_mario_blue)
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        self.life_image = self.font.render(str(self.stats.lives_left), True, self.text_color,
                                           self.settings.color_mario_blue)
        self.life_rect.left = self.screen_rect.left + 20
        self.life_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.life_image, self.life_rect)
