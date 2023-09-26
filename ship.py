import pygame


class Ship():
    def __init__(self, ai_setting,  screen):
        """Init ship and set him begining position"""
        self.screen = screen
        self.ai_setting = ai_setting
        #Load ship picture and get rectangle
        self.image = pygame.image.load('images/micro_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Every new ship appear near bottom edge of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position based on flag"""
        if self.moving_right:
            self.rect.centerx += 1
            #self.center += self.ai_setting.ship_speed_factor
        if self.moving_left:
            self.rect.centerx -= 1
            #self.center -= self.ai_setting.ship_speed_factor
        #self.rect.centerx -= self.center

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)
