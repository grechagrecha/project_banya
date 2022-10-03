import sys
import pygame

from settings.settings_management import get_resolution, get_framerate
from player import Player


class Game:
    def __init__(self):
        pygame.init()

        self._resolution = get_resolution()
        self._framerate = get_framerate()

        # self.player_sprite = pygame.sprite.GroupSingle()
        # self.player = Player((320, 160), self.player_sprite)

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

            # self.player_sprite.draw(self.screen)

            pygame.display.update()

            dt = self.clock.tick(self._framerate) / 1000
