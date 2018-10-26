import pygame
import sys


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("EXITING")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print("KEY DOWN")
        elif event.type == pygame.KEYUP:
            print("KEY UP")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print("CLICK AT", mouse_x, mouse_y)
