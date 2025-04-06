import pygame
import random

class Ghost:
    def __init__(self, x, y, size=30):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 0, 0)
        self.speed = 2

        # 👇 Direction is a tuple like (1, 0), (0, 1), etc.
        self.direction = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
        self.steps = random.randint(30, 100)  # How long it moves in one direction

    def move(self):
        # Move in current direction
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
        self.steps -= 1

        # 👇 Change direction randomly after a few steps
        if self.steps <= 0:
            self.direction = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
            self.steps = random.randint(30, 100)

        # Bounce off walls
        if self.x <= 50 or self.x >= 750:
            self.direction = (-self.direction[0], self.direction[1])
        if self.y <= 50 or self.y >= 550:
            self.direction = (self.direction[0], -self.direction[1])

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
