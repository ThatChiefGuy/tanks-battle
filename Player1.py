
class Player:
    def __init__(self, pygame, random):
        self.player = pygame.Rect(500, 500, 30, 50)
        self.pygame = pygame
        self.random = random

    def movement(self, keys_pressed):
        if keys_pressed[ord("w")]:
            self.player.y -= 5

        if keys_pressed[ord("a")]:
            self.player.x -= 5

        if keys_pressed[ord("s")]:
            self.player.y += 5

        if keys_pressed[ord("d")]:
            self.player.x += 5
