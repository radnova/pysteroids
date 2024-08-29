import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.color = (251, 215, 20)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, SHOT_RADIUS, 5)

    def update(self, dt):
        self.position += self.velocity * dt