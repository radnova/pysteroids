import pygame
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0,255))
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        frags = 2
        neo_r = self.radius // 2

        for _ in range(frags):
            offset = pygame.Vector2(
                random.uniform(-1, 1), random.uniform(-1, 1)
            ).normalize() * neo_r
            neo_p = self.position + offset

            frag = Asteroid(neo_p.x, neo_p.y, neo_r)

            frag.velocity = self.velocity.rotate(random.uniform(-30, 30)) * 1.2
        