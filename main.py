import pygame
import random
from pygame import mixer
import Player1
import Computer

pygame.init()
mixer.init()

mixer.music.load("running.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

Screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Tanks")


player_imports = Player1.Player(pygame, 500, 500)
computer_imports = Computer.Computer(pygame, player_imports.player, random)

Red = (255, 0, 0)
Blue = (0, 0, 255)
White = (250, 250, 250)
FPS = 60


def draw():
    Screen.fill(White)
    pygame.draw.rect(Screen, Red, player_imports.player)
    pygame.draw.rect(Screen, Blue, computer_imports.computer)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        player_imports.movement(keys_pressed)

        computer_imports.following_motion()
        computer_imports.unfollowing_motion()

        draw()
    pygame.quit()


if __name__ == "__main__":
    main()
