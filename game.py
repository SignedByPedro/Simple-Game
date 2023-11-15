import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 300
GROUND_HEIGHT = 50
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

# Load images
background_img = pygame.image.load("background.png")
dino_img = pygame.image.load("dino.gif")
cactus_img = pygame.image.load("cactus.gif")
obstacle_img = pygame.image.load("obstacle.gif")  # Load the new obstacle image directly with Pygame

# Resize images
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
dino_img = pygame.transform.scale(dino_img, (50, 50))
cactus_img = pygame.transform.scale(cactus_img, (30, 30))
obstacle_img = pygame.transform.scale(obstacle_img, (30, 30))  # Resize the new obstacle image

# Game variables
dino_x = 50
dino_y = HEIGHT - GROUND_HEIGHT - dino_img.get_height()
dino_speed = 5

cactus_x = WIDTH
cactus_y = HEIGHT - GROUND_HEIGHT - cactus_img.get_height()

obstacle_x = WIDTH
obstacle_y = HEIGHT - GROUND_HEIGHT - obstacle_img.get_height()

clock = pygame.time.Clock()

# Function to spawn either cactus or obstacle
def spawn_obstacle():
    obstacle_type = random.choice(["cactus", "obstacle"])
    x = WIDTH
    y = HEIGHT - GROUND_HEIGHT - (cactus_img.get_height() if obstacle_type == "cactus" else obstacle_img.get_height())
    return obstacle_type, x, y

# Initial spawns
cactus, cactus_x, cactus_y = spawn_obstacle()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and dino_y == HEIGHT - GROUND_HEIGHT - dino_img.get_height():
        dino_y -= 150

    # Update game logic
    dino_y = min(dino_y + dino_speed, HEIGHT - GROUND_HEIGHT - dino_img.get_height())
    cactus_x -= 5
    obstacle_x -= 5

    if cactus_x + cactus_img.get_width() < 0:
        cactus, cactus_x, cactus_y = spawn_obstacle()

    if obstacle_x + obstacle_img.get_width() < 0:
        cactus, obstacle_x, obstacle_y = spawn_obstacle()

    # Check for collisions
    if (
        (dino_x < cactus_x + cactus_img.get_width() and
         dino_x + dino_img.get_width() > cactus_x and
         dino_y < cactus_y + cactus_img.get_height() and
         dino_y + dino_img.get_height() > cactus_y) or
        (dino_x < obstacle_x + obstacle_img.get_width() and
         dino_x + dino_img.get_width() > obstacle_x and
         dino_y < obstacle_y + obstacle_img.get_height() and
         dino_y + dino_img.get_height() > obstacle_y)
    ):
        print("Game Over!")
        running = False

    # Draw to the screen
    screen.blit(background_img, (0, 0))  # Draw the background first
    screen.blit(dino_img, (dino_x, dino_y))
    screen.blit(cactus_img if cactus == "cactus" else obstacle_img, (cactus_x, cactus_y))

    pygame.draw.rect(screen, BLACK, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()