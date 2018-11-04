import pygame
import pygame.mixer

pygame.mixer.init()

sounds = []

mario_jump = pygame.mixer.Sound("media/sounds/mario/jump.wav")  # [0] Mario jumping
sounds.append(mario_jump)


def play(request):
    pygame.mixer.Sound.play(sounds[request])
