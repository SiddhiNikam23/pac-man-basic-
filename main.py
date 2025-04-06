import pygame  # Import pygame for building the game
from config import *  # Import all constants from config.py
from map import draw_map  # Function to draw the custom map
from pacman import Pacman  # Pacman class
from ghost import Ghost  # Ghost class
import math

# Initialize pygame
pygame.init()

# Create the main screen (game box) with given dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set game title
pygame.display.set_caption("Creative Pac-Man")

# Load background image
background = pygame.image.load("assets/background.jpg")

# Create clock for controlling FPS
clock = pygame.time.Clock()

# Create Pacman object
pacman = Pacman(100,100)

# Create multiple ghosts with unique sizes
ghosts = [
    Ghost(600, 400, 30),
    Ghost(700, 200, 20),
    Ghost(650, 300, 40)
]

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))  # Draw background on screen

    draw_map(screen)  # Draw custom map with Siddhi structure

    for event in pygame.event.get():  # Check events
        if event.type == pygame.QUIT:
            running = False  # Stop the loop when window is closed

    pacman.move()  # Update pacman's position
    pacman.draw(screen)  # Draw pacman on screen

    for ghost in ghosts:  # Loop through each ghost
        ghost.move()  # Update ghost position (placeholder logic for now)
        ghost.draw(screen)
        # 👇 Check if Pac-Man collides with a ghost
        distance = math.hypot(pacman.x - ghost.x, pacman.y - ghost.y)
        if distance < pacman.radius + ghost.size:
           print("Pac-Man got caught!")
           running = False  # End the game
        
        
        
          # Draw each ghost on screen

    pygame.display.update()  # Update the full screen
    clock.tick(FPS)  # Limit frame rate to FPS

pygame.quit()  # Quit pygame when done
