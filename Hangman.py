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
                game_running = False

        # Draw on the game screen
        game_screen.fill(BLACK)
        text = font.render("Welcome to Hangman!", True, WHITE)
        game_screen.blit(text, (210, HEIGHT//2 - 44))
        text = font.render("(press SPACE to continue)", True, WHITE)
        game_screen.blit(text, (185, HEIGHT // 2 - 2))
        pygame.display.flip()

def main():
    print("a")

if __name__ == "__main__":
    run_game_screen()