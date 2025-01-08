import pygame
from constants import ASTEROID_LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20.0, 50.0)
        spawn_velocity1 = self.velocity.rotate(random_angle)
        spawn_velocity2 = self.velocity.rotate(- random_angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        spawn_asteroid1 = Asteroid(self.position[0], self.position[1], smaller_radius)
        spawn_asteroid2 = Asteroid(self.position[0], self.position[1], smaller_radius)
        spawn_asteroid1.velocity = spawn_velocity1 * 1.2
        spawn_asteroid2.velocity = spawn_velocity2 * 1.2