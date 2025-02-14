import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self,ai_game):
        super().__init__()
        """Initializing the ship and setting the starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings=ai_game.settings
        self.path = ai_game.path

        #Loading the ship image
        self.image = pygame.image.load(self.path+"/Images/ship.png")
        self.rect = self.image.get_rect()

        #Starrtingeach new ship at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y = self.rect.bottom - 90 
          
        #Stores a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        

    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        #Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """Draw a ahip at the current location"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        # self.rect.y = self.screen_rect.bottom
        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.y = self.rect.bottom - 90 
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        