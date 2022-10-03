import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()

        self._resolution = (1280, 720)
        self._framerate = 144

        self.screen = pygame.display.set_mode(self._resolution)
        pygame.display.set_caption('project banya')

        self.clock = pygame.time.Clock()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('grey')
            pygame.display.update()

            self.clock.tick(self._framerate)


if __name__ == '__main__':
    game = Game()
    game.run()
