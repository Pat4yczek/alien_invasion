import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Main class intended for resource menagment and how game's works"""
    def __init__(self):
        """Initialization of game and creating its resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.srceen_heght))
        pygame.display.set_caption("Alien Invasion")
        # Define the background color
    
    def run_game(self):
        """Beginning of game's main loop"""
        while True:
            # Waiting for click button or click mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            # Displaying the last modified screen
            pygame.display.flip()

if __name__ == "__main__":
    # Creating copy of the game and launch it
    ai = AlienInvasion()
    ai.run_game()