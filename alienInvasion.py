import sys
import pygame

class AlienInvasion:

    """Class that manages game assets and behaviours"""
    def __init__(self) -> None:
        
        """Initialize the Gane, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        #Set Background Color 
        self.bg_color = (108, 22, 128)

    def run_game(self):

        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            #Draw the most recent screen
            pygame.display.flip()
            self.clock.tick(60)
    

#This is the main function
    
if __name__ == '__main__':

    ai = AlienInvasion()
    ai.run_game()
  
   
 
                    
