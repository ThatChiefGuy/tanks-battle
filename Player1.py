
class Player:
    def __init__(self, pygame, position_x, position_y):
        self.player = pygame.Rect(position_x, position_y, 30, 50)
        self.pygame = pygame

    def movement(self, keys_pressed):

        if keys_pressed[ord("w")]:
            self.player.y -= 10

        if keys_pressed[ord("a")]:
            self.player.x -= 10

        if keys_pressed[ord("s")]:
            self.player.y += 10

        if keys_pressed[ord("d")]:
            self.player.x += 10
