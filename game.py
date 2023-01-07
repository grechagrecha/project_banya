import pygame

from settings.settings_management import get_resolution, get_framerate
from player import Player
from event_handler import EventHandler
from debug import Debug


class Game:
    def __init__(self, *, debug_mode=False):
        pygame.init() if not pygame.init() else ...

        self._resolution = get_resolution()
        self._framerate = get_framerate()

        self.player_sprite = pygame.sprite.GroupSingle()

        self.player = Player((320, 160), self.player_sprite)
        self.event_handler = EventHandler(self.player)

        self.screen = pygame.display.set_mode(self._resolution)
        pygame.display.set_caption('project banya')

        self.clock = pygame.time.Clock()
        self.dt = None

        self.debug = Debug() if debug_mode else None

    def update(self):
        self.player_sprite.update(self.dt)
        pygame.display.update()

        self.dt = self.clock.tick(self._framerate) / 1000

    def draw(self):
        """ Main draw function """

        self.screen.fill('grey')

        self.player_sprite.draw(self.screen)

        if self.debug:
            self.debug.show_debug(
                f'dir: {self.player.movement.direction} |',
                f'pos: {self.player.pos.x:.1f} {self.player.pos.y:.1f} |',
                f'vel: {self.player.movement.velocity.x:.1f} {self.player.movement.velocity.y:.1f}|',
                f'is_mov: {self.player.movement.moving} |'
                f'vel_mag: {self.player.movement.velocity.magnitude():.3f}'
            )

    def run(self):
        """ Main game loop """

        # Initial dt calculation
        self.dt = self.clock.tick(self._framerate) / 1000

        while True:
            self.event_handler.run()

            self.update()
            self.draw()
