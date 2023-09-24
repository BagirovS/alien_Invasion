import pygame


class Ship():
    def __init__(self, screen):
        """Init ship and set him initial position"""
        self.screen = screen

        #Load ship picture and get rectangle
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Every new ship appear near bottom edge of screen
        self.rect.centerx = self.screen_rect.centrex
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)
