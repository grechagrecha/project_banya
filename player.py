import pygame


from pygame.math import Vector2


from constants import PLAYER_SPEED


class Direction(Vector2):
    def __init__(self):
        super().__init__()
        self.last_dir = Vector2()
        self.stop = False

    def set(self, x, y):
        if not (x or y):
            self.last_dir.update(x, y)
            self.stop = True
        else:
            self.stop = False
        self.x, self.y = x, y


class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos: tuple, group: pygame.sprite.GroupSingle):
        super().__init__(group)

        # initial setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('black')
        self.rect = self.image.get_rect(center=start_pos)

        self.direction = Direction()
        self.pos = Vector2(*start_pos)
        self.max_speed = PLAYER_SPEED
        self.velocity = 0
        self.acceleration = 0.1

    def move(self, dt):
        if self.direction.magnitude() != 0:
            self.direction.normalize_ip()
        if self.direction.x or self.direction.y:
            self.acceleration = 0.5
        else:
            self.acceleration = -0.5

        self.velocity += self.acceleration
        self.pos += self.direction * self.velocity * dt
        self.rect.center = self.pos

    def update(self, dt):
        self.move(dt)
