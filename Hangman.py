import pygame
import sys

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 100)
RED = (100, 0, 0)
GREEN = (0, 100, 0)

font = pygame.font.SysFont(None, 48)

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

if __name__ == "__main__":
    run_game_screen()