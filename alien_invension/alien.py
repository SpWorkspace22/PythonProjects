import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent alien """
    def __init__(self,ai_settings,screen):
        """INitialize alien and set its starting position"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien image 
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        #start each new alien at top left 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        #Store the aliens position
        self.x = float(self.rect.x)


    def blitme(self):
        self.screen.blit(self.image,self.rect) 

    def update(self):
        """Move the align right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return true if alien is at edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
