import pygame
import random
import Player1
import Computer

pygame.init()

Screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Tanks")


player_imports = Player1.Player(pygame, random)
computer_imports = Computer.Computer(pygame, player_imports.player)

Red = (255, 0, 0)
Blue = (0, 0, 255)
White = (250, 250, 250)
FPS = 60


def draw():
    Screen.fill(White)
    pygame.draw.rect(Screen, Red, player_imports.player)
    pygame.draw.rect(Screen, Blue, computer_imports.player2)
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
        draw()
    pygame.quit()


if __name__ == "__main__":
    main()
