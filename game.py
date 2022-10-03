import sys
import pygame

from settings.settings_management import get_resolution, get_framerate


class Game:
    def __init__(self):
        pygame.init()

        self._resolution = get_resolution()
        self._framerate = get_framerate()

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

            dt = self.clock.tick(self._framerate) / 1000
