import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):
    """A Class to manage bullet """
    def __init__(self,ai_setting,screen,ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a bullet rect at (0,0) and  set correct possition
        self.rect = pygame.Rect(0,0, ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store bullets position as decimal value
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        """Move bullet upwords"""
        self.y -= self.speed_factor
        
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        

