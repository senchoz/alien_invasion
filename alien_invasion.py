import sys
import pygame

class AlienInvasion:
    """A class for managing game resources and behavior."""

    def __init__(self):
        """Initializes the game and assigns game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Run the main loop."""
        while True:
            # Watch for keyboard and mouse events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Shows the last frame
            pygame.display.flip()

if __name__ == '__main__':
    # Create a class instance.
    ai = AlienInvasion()
    # Run the game.
    ai.run_game()
