import pygame
import sys

from player import Player


class EventHandler:
    def __init__(self, player: Player):
        self._keys = pygame.key.get_pressed()
        self._events = pygame.event.get()
        self._player = player

    def _handle_events(self):
        for event in self._events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _handle_keys(self):
        if self._keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        self._player.movement.set_direction(
            x=self._keys[pygame.K_d] - self._keys[pygame.K_a],
            y=self._keys[pygame.K_s] - self._keys[pygame.K_w]
        )

    def _update(self):
        self._keys = pygame.key.get_pressed()
        self._events = pygame.event.get()

    def run(self):
        self._update()
        self._handle_events()
        self._handle_keys()
