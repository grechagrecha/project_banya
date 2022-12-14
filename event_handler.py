import pygame
import sys


def handle_events(player):
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

    player.direction.x = keys[pygame.K_d] - keys[pygame.K_a]
    player.direction.y = keys[pygame.K_s] - keys[pygame.K_w]
