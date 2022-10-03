import pygame


from constants import PLAYER_SPEED


class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos: tuple, group: pygame.sprite.GroupSingle):
        super().__init__(group)

        # initial setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('black')
        self.rect = self.image.get_rect(center=start_pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(*start_pos)
        self.speed = PLAYER_SPEED

    def move(self, dt):
        if self.direction:
            self.direction.normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def update(self, dt):
        self.move(dt)
