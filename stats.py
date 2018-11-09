
class Stats:

    def __init__(self):
        self.coins = None
        self.high_score = None
        self.lives_left = None
        self.score = None
        self.world = None
        self.import_high_score()
        self.reset_stats()

    def reset_stats(self):
        self.coins = 0
        self.lives_left = 3
        self.score = 0
        self.world = (1, 1)

    def import_high_score(self):
        data = open('high_score.txt', 'r')
        if data:
            self.high_score = int(data.read())
            print("Success importing high score: " + str(self.high_score))
        else:
            print("Error importing high score")
