import pygame

from pygame.math import Vector2
from math import copysign, sqrt

from constants import PLAYER_MAX_SPEED, PLAYER_ACCELERATION, PLAYER_FRICTION


class Movement:
    def __init__(self):
        self.direction = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.moving = False
        self.max_speed = PLAYER_MAX_SPEED
        self.acceleration = PLAYER_ACCELERATION
        self.friction = PLAYER_FRICTION

        self.dt = None

    def set_direction(self, x=0, y=0):
        # Normalizing vector for diagonal movement
        if self.direction.magnitude() > 1:
            self.direction.normalize_ip()
        self.direction.update(x, y)

        self.moving = True if self.direction else False

    def _calculate_speed(self):
        if self.direction.x:
            self.velocity.x += self.acceleration * self.direction.x * self.dt
        else:
            if self.velocity.x < 0:
                self.velocity.x += self.friction * self.dt
            elif self.velocity.x > 0:
                self.velocity.x -= self.friction * self.dt

            if abs(self.velocity.x) < 0.25:
                self.velocity.x = 0

        if abs(self.velocity.x) > self.max_speed:
            self.velocity.x = self.max_speed * copysign(1, self.velocity.x)

        if self.direction.y:
            self.velocity.y += self.acceleration * self.direction.y * self.dt
        else:
            if self.velocity.y < 0:
                self.velocity.y += self.friction * self.dt
            elif self.velocity.y > 0:
                self.velocity.y -= self.friction * self.dt

            if abs(self.velocity.y) < 0.25:
                self.velocity.y = 0

        if abs(self.velocity.y) > self.max_speed:
            self.velocity.y = self.max_speed * copysign(1, self.velocity.y)

        if self.velocity.magnitude() > self.max_speed:
            self.velocity = self.velocity.lerp(self.direction, 0.1)

    def update(self, dt):
        self.dt = dt

        self._calculate_speed()


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
        self.movement.update(dt)

        self.pos += self.movement.velocity
        self.rect.center = self.pos

    def update(self, dt):
        self.move(dt)
