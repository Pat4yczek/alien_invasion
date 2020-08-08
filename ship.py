import pygame
class Ship:
    """Class designed to manage of space ship"""
    def __init__(self, ai_game):
        """Initialization of space ship and its start coordinates"""
        self.screen = ai_game.screen
        self.sreen_rect = ai_game.screen.get_rect()
        # Loading a space ship's image ang get its coordinates
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Each new space ship appears at the bottom if screen.
        self.rect.midbottom = self.sreen_rect.midbottom

    def blitme(self):
        """Displaying space ship in its current position"""
        self.screen.blit(self.image, self.rect)

    