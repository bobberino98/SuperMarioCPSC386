import pygame
import sys


<<<<<<< HEAD
def check_events(mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("EXITING")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print("KEY DOWN")
            if event.key == pygame.K_LEFT:
                print("Key left")
                mario.direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                print("Key right")
                mario.direction = "RIGHT"
        elif event.type == pygame.KEYUP:
            print("KEY UP")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print("CLICK AT", mouse_x, mouse_y)
=======
class Controller:
    def __init__(self, mario):
        self.mario = mario

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("EXITING")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("KEY DOWN")
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                print("KEY UP")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print("CLICK AT", mouse_x, mouse_y)

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
        elif event.key == pygame.K_UP:
            self.mario.moving_up = True
            self.mario.moving_left = False
            self.mario.moving_down = False
            self.mario.moving_right = False

        elif event.key == pygame.K_DOWN:
            self.mario.moving_down = True
            self.mario.moving_left = False
            self.mario.moving_right = False
            self.mario.moving_up = False
        elif event.key == pygame.K_q:
            self.mario.create_portal(1)
        elif event.key == pygame.K_e:
            self.mario.create_portal(2)
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
>>>>>>> 41ec6b6ce53e639f47278ed5c854a873f15e4204
