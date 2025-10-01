import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Screen One")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GREEN = (0, 200, 100)

# Fonts
font = pygame.font.SysFont(None, 48)

# Function to run the separate game screen
def run_game_screen():
    game_running = True
    game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game Screen")

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_running = False  # Return to main screen

        # Draw on the game screen
        game_screen.fill(GREEN)
        text = font.render("Game Screen - Press SPACE to go back", True, WHITE)
        game_screen.blit(text, (50, HEIGHT//2 - 24))
        pygame.display.flip()

# Main loop
def main():
    running = True

    while running:
        screen.fill(BLUE)
        text = font.render("Main Screen - Press SPACE to Start", True, WHITE)
        screen.blit(text, (50, HEIGHT//2 - 24))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                run_game_screen()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()