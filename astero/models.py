from pygame.math import Vector2
from pygame.transform import rotozoom

from utils import load_sprite_from_sheet, wrap_position

UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position) 
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)
        
    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)
        
    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)
        
    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius
 
class Spaceship(GameObject):
    MANEUVERABILITY = 3
    ACCELERATION = 0.25

    def __init__(self, position):
        self.direction = Vector2(UP)
        super().__init__(position, load_sprite_from_sheet("spaceship", (40, 0, 40, 40)), Vector2(0))
    
    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)
    
    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
