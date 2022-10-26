import pygame
import Player1

pygame.init()

Screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Tanks")

player_imports = Player1.Player(pygame)

Red = (255, 0, 0)
White = (250, 250, 250)
FPS = 60


def draw():
    Screen.fill(White)
    pygame.draw.rect(Screen, Red, player_imports.player)
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
        mouse_position = pygame.mouse.get_pos()
        player_imports.mouse(mouse_position)
        player_imports.movement(keys_pressed)
        draw()
    pygame.quit()


if __name__ == "__main__":
    main()
