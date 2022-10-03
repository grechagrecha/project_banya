import pygame

from settings.settings_management import get_resolution, get_framerate
from player import Player
from event_handler import handle_events
from debug import Debug


class Game:
    def __init__(self, *, debug_mode=False):
        pygame.init()

        self._resolution = get_resolution()
        self._framerate = get_framerate()

        self.player_sprite = pygame.sprite.GroupSingle()

        self.player = Player((320, 160), self.player_sprite)

        self.screen = pygame.display.set_mode(self._resolution)
        pygame.display.set_caption('project banya')

        self.clock = pygame.time.Clock()

        self.debug = None
        if debug_mode:
            self.debug = Debug()

    def run(self):

        # Initial dt calculation
        dt = self.clock.tick(self._framerate) / 1000

        while True:
            handle_events(self.player)

            self.screen.fill('grey')

            self.player_sprite.draw(self.screen)

            self.player_sprite.update(dt)

            if self.debug:
                self.debug.show_debug(self.player.direction, self.player.pos)

            pygame.display.update()

            dt = self.clock.tick(self._framerate) / 1000
