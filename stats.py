
class Stats:

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.lives_left = 3
        self.score = 0
        self.level = 1

    def reset_stats(self):
        self.lives_left = 3
        self.score = 0
        self.level = 1
