import pygame
import pygame.mixer

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

sounds = []

mario_jump = pygame.mixer.Sound("media/sounds/mario/jump.wav")  # [0] Mario jumping
mario_jump.set_volume(.05)
sounds.append(mario_jump)


def play(request):
    pygame.mixer.Sound.play(sounds[request])
