import pygame
from config import YELLOW

class Pacman:
    def __init__(self,x,y):
        # Starting position of Pac-Man
        self.x = 100
        self.y = 100
        self.speed = 4  # Movement speed
        self.radius = 15  # Size of Pac-Man
        self.color = (255, 255, 0)
        self.speed = 5

    def move(self):
        # Get the pressed keys
        keys = pygame.key.get_pressed()

        # Move in the direction of the pressed arrow key
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, screen):
        # Draw Pac-Man as a yellow circle
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)
