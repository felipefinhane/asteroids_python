import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_angle = random.uniform(20, 50)
            asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, new_angle) * 1.2
            asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -new_angle) * 1.2
        self.split()
