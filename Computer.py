
class Computer:
    def __init__(self, pygame, player, random):
        self.computer = pygame.Rect(500, 200, 30, 50)
        self.following = True
        self.player = player
        self.chance = 1
        self.pygame = pygame
        self.random = random

    def following_motion(self):
        if self.following:
            if self.player.x > self.computer.x:
                self.computer.x += 3

            if self.player.x < self.computer.x:
                self.computer.x -= 3

            if self.player.y > self.computer.y:
                self.computer.y += 2

            if self.player.y < self.computer.y:
                self.computer.y -= 2

    def unfollowing_motion(self):

        self.chance = self.random.randint(1, 100)

        if self.chance == 5:
            self.following = False

        if not self.following:

            if self.player.x > self.computer.x:
                self.computer.x -= 3

            if self.player.x < self.computer.x:
                self.computer.x += 3

            if self.player.y > self.computer.y:
                self.computer.y -= 3

            if self.player.y < self.computer.y:
                self.computer.y += 3

            self.chance = self.random.randint(1, 30)

            if self.chance == 6:
                self.following = True
