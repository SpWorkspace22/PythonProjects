import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Create Ship and related settings """

    def __init__(self, ai_settings,screen):
        """Initalize the ship"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the image
        self.image = pygame.image.load("images/space-ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()


        #Start each ship at botton and center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        #Movemnet flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed

        self.rect.centerx = self.center

    def blitme(self):
        """Draw Ship """
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Center the ship on screen."""
        self.center = self.screen_rect.centerx
