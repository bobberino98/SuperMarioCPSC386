import pygame


class Stats:

    def __init__(self):
        self.coins = None
        self.high_score = None
        self.last_time_update = None
        self.lives_left = None
        self.score = None
        self.time = None  # Time remaining for user to complete the game
        self.world = None
        self.import_high_score()
        self.reset_stats()

    def reset_stats(self):
        self.coins = 0
        self.last_time_update = 0
        self.lives_left = 3
        self.score = 0
        self.time = 401
        self.world = (1, 1)

    def update(self):
        if self.score > self.high_score:
            print("Updating high score records to " + str(self.high_score) + ", congratulations!")
            self.high_score = self.score
            data = open('high_score.txt', 'w')
            data.write(str(self.high_score))
        if pygame.time.get_ticks() - self.last_time_update > 520:
            self.last_time_update = pygame.time.get_ticks()
            self.time -= 1

    def import_high_score(self):
        data = open('high_score.txt', 'r')
        if data:
            self.high_score = int(data.read())
            print("Success importing high score: " + str(self.high_score))
        else:
            print("Error importing high score")
