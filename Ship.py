import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.image=pygame.image.load("ship.bmp")
        self.ship_speed_factor=4

        #get initial coordinates for Image (ship) and screen coordiantes
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        # initializing ship at bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.moving_right=False
        self.moving_left=False


    def update(self):

        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += self.ship_speed_factor

        if self.moving_left and self.rect.left>0:
            self.rect.centerx -= 4


    # Draw ship

    def blitme(self):
        self.screen.blit(self.image,self.rect)




