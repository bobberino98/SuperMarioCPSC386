import pygame
import sys



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


class Controller:
    def __init__(self, mario):
        self.mario = mario

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                sys.exit()
            elif event.type == pygame.KEYDOWN:

                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()


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

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.mario.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.mario.moving_left = False
        elif event.key == pygame.K_UP:
            self.mario.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.mario.moving_down = False
