import pygame

class Ship():
    """Class for ship control"""

    def __init__(self, ai_game):
        """Initializes the ship, sets its position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
