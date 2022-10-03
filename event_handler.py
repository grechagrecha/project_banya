import pygame
import sys

# for reference
from player import Player


def handle_events(player: Player):
    handle_keys(player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def handle_keys(player):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if keys[pygame.K_w]:
        player.direction.y = -1
    elif keys[pygame.K_s]:
        player.direction.y = 1
    else:
        player.direction.y = 0

    if keys[pygame.K_a]:
        player.direction.x = -1
    elif keys[pygame.K_d]:
        player.direction.x = 1
    else:
        player.direction.x = 0
