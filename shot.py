import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, ASTEROID_LINE_WIDTH

class Shot(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, ASTEROID_LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)