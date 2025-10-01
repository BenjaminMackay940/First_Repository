import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Enemy")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Set up player and enemy
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size]

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

clock = pygame.time.Clock()
random_int = random.randint(1,10)
random_int2 = random.randint(1,10)

# Main game loop
game_over = False
while not game_over:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= random_int
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += random_int2
    '''if keys[pygame.K_DOWN] and player_pos[0] > 0:
        player_pos[0] -= random_int
    if keys[pygame.K_RIGHT] and player_pos[0] < HEIGHT - player_size:
        player_pos[0] += random_int2
'''
    # Move enemy
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)

    # Collision detection
    if (
        enemy_pos[1] < player_pos[1] + player_size
        and enemy_pos[1] + enemy_size > player_pos[1]
        and enemy_pos[0] < player_pos[0] + player_size
        and enemy_pos[0] + enemy_size > player_pos[0]
    ):
        game_over = True

    # Draw player and enemy
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, GREEN, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    pygame.display.flip()
    clock.tick(30)

print("Game Over!")
