import pygame
from config import BLUE

# Function to draw walls in a simple creative way
def draw_map(screen):
    # Draw outer walls
    pygame.draw.rect(screen, BLUE, (50, 50, 700, 10))  # Top wall
    pygame.draw.rect(screen, BLUE, (50, 540, 700, 10))  # Bottom wall
    pygame.draw.rect(screen, BLUE, (50, 50, 10, 500))  # Left wall
    pygame.draw.rect(screen, BLUE, (740, 50, 10, 500))  # Right wall

    # Add simple Siddhi temple structure (like a tiered pyramid) at the center
    pygame.draw.rect(screen, BLUE, (360, 200, 80, 10))  # Base tier
    pygame.draw.rect(screen, BLUE, (370, 180, 60, 10))  # Mid tier
    pygame.draw.rect(screen, BLUE, (380, 160, 40, 10))  # Top tier

    # Add some inner creative walls
    pygame.draw.rect(screen, BLUE, (150, 150, 100, 10))
    pygame.draw.rect(screen, BLUE, (550, 150, 100, 10))
    pygame.draw.rect(screen, BLUE, (150, 400, 100, 10))
    pygame.draw.rect(screen, BLUE, (550, 400, 100, 10))

    # Add dots (pellets) across the screen
    for x in range(70, 740, 40):  # Loop for x positions
        for y in range(70, 530, 40):  # Loop for y positions
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 3)  # White dot

