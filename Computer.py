
class Computer:
    def __init__(self, pygame, player):
        self.player2 = pygame.Rect(500, 200, 30, 50)
        self.pygame = pygame
        self.player = player

    def following_motion(self):
        if self.player.x > self.player2.x:
            self.player2.x += 3

        if self.player.x < self.player2.x:
            self.player2.x -= 3

        if self.player.y > self.player2.y:
            self.player2.y += 2

        if self.player.y < self.player2.y:
            self.player2.y -= 2
