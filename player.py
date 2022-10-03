import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos: tuple, group: pygame.sprite.GroupSingle):
        super().__init__(group)

        # initial setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('black')
        self.rect = self.image.get_rect(center=start_pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2()
