import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initializes game and create object screen
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Ship(screen)
    #Create ship
    ship = Ship(screen)

    #Start the main cycle of game
    while True:
        gf.check_events()
        gf.update_screen(ai_setting, screen, ship)


run_game()

