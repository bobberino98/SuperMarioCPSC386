import pygame
import pygame.mixer

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# [0] Mario jumping
sounds = []

mario_jump = pygame.mixer.Sound("media/sounds/mario/jump.wav")
mario_jump.set_volume(.20)
sounds.append(mario_jump)


def play(request):
    pygame.mixer.Sound.play(sounds[request])
