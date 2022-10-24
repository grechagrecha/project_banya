import pygame

from pygame.math import Vector2

from constants import PLAYER_SPEED


class Movement:
    def __init__(self):
        super().__init__()
        self.direction = Vector2()
        self.stopped = False
        self.max_speed = PLAYER_SPEED
        self.speed = 0
        self.acceleration = 4

    def __configure_direction(self, **kwargs):
        x, y = kwargs.get('x'), kwargs.get('y')

        self.direction.update(x, y)

        if self.direction.magnitude() != 0:
            self.direction.normalize_ip()
        if self.is_stopped():
            pass

    def set_direction(self, x=0, y=0):
        if not (x or y):
            self.stopped = True
        else:
            self.__configure_direction(x=x, y=y)
            self.stopped = False

    def __calculate_speed(self):
        if self.is_stopped():
            if self.speed > 0:
                self.speed -= self.acceleration
        elif self.speed <= self.max_speed - self.acceleration:
            self.speed += self.acceleration

    def get_pos_shift(self, dt):
        self.__calculate_speed()
        return self.direction * self.speed * dt

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

    def move(self, dt):
        self.pos += self.movement.get_pos_shift(dt)
        self.rect.center = self.pos

    def update(self, dt):
        self.move(dt)
