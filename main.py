import pygame, sys
from settings import *

# debug test (pass)
# from debug import debug

class Game:
    def __init__(self):

        # first pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('Black')

            # debug test (pass)
            # debug('hello')

            pygame.display.update()
            self.clock.tick(FPS)
if __name__ == '__main__':
    game = Game()
    game.run()