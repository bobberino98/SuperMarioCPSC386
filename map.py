from pygame.sprite import Group
from brick import Brick


class Map:
    def __init__(self, screen, settings):
        super(Map, self).__init__()
        self.brick_count = 80  # number of bricks to initially render
        self.brick_columns = []
        self.settings = settings
        self.screen = screen
        for x in range(18):  # start with 18 columns of bricks
            self.add_column()

    def add_column(self):  # create a new column of bricks
        new_column = Group()
        if len(self.brick_columns) == 0:
            x = 0
        else:
            x = 75 * len(self.brick_columns)
        for i in range(4):
            brick = Brick(self.screen)
            brick.rect.x = x
            brick.rect.y = self.settings.brick_y_offset + (75 * i)
            new_column.add(brick)
        self.brick_columns.append(new_column)

    def blitme(self):   # blit everything on the map
        for column in self.brick_columns:   # blit all bricks
            for brick in column:
                self.screen.blit(brick.image, brick.rect)
