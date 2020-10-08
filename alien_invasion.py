#!/usr/bin/python3

import sys
import pygame

from settings import Settings

class AlienInvasion:
    """A class for managing game resources and behavior."""

    def __init__(self):
        """Initializes the game and assigns game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230) # set background to almost white

    def run_game(self):
        """Run the main loop."""
        while True:
            # Watch for keyboard and mouse events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen on each loop cycle
            # and fill it with the set color
            self.screen.fill(self.settings.bg_color)

            # Shows the last frame
            pygame.display.flip()

if __name__ == '__main__':
    # Create a class instance.
    ai = AlienInvasion()
    # Run the game.
    ai.run_game()
