import pygame
import sys


class Controller:
    def __init__(self, mario, settings):
        self.mario = mario
        self.settings = settings

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.mario.moving_right = True
            self.mario.moving_left = False
            self.mario.moving_up = False
            self.mario.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.mario.moving_left = True
            self.mario.moving_right = False
            self.mario.moving_up = False
            self.mario.moving_down = False
        elif event.key == pygame.K_UP and not self.mario.jump_start:
            self.mario.jumping = True
        elif event.key == pygame.K_m:
            self.settings.muted = not self.settings.muted
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.mario.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.mario.moving_left = False
        elif event.key == pygame.K_UP:
            self.mario.jumping = False
