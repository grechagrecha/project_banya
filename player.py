import pygame


from pygame.math import Vector2


from constants import PLAYER_SPEED


class Movement:
    def __init__(self):
        super().__init__()
        self.direction = Vector2()
        self.stopped = False

    def __configure_direction(self, x, y):
        self.direction.update(x, y)
        if self.direction.magnitude() != 0:
            self.direction.normalize_ip()

    def set_direction(self, x, y):
        if not (x or y):
            self.stopped = True
        else:
            self.__configure_direction(x, y)
            self.stopped = False

    def is_stopped(self):
        return self.stopped


class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos: tuple, group: pygame.sprite.GroupSingle):
        super().__init__(group)

        # initial setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('black')
        self.rect = self.image.get_rect(center=start_pos)

        self.movement = Movement()
        self.pos = Vector2(*start_pos)
        self.max_speed = PLAYER_SPEED
        self.velocity = 0
        self.acceleration = 4

    def move(self, dt):
        if self.movement.is_stopped():
            if self.velocity > 0:
                self.velocity -= self.acceleration
        elif self.velocity <= self.max_speed:
            self.velocity += self.acceleration

        self.pos += self.movement.direction * self.velocity * dt
        self.rect.center = self.pos

    def update(self, dt):
        self.move(dt)
