from pygame.math import Vector2

from utils import load_sprite_from_sheet

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position) 
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)
        
    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)
        
    def move(self):
        self.position = self.position + self.velocity
        
    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius
 
class Spaceship(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite_from_sheet("spaceship", (40, 0, 40, 40)), Vector2(0))
