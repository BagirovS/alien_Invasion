import sys
import pygame
from setting import Settings

def run_game():
    #Initializes game and create object screen
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Screen color assignment
    bg_color = (100, 78, 230)

    #Launch the main cycle of game
    while True:
        screen.fill(ai_setting.bg_color)
        #Tracking events on keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                sys.exit()

        #Display the last drawn screen
        pygame.display.flip()

run_game()

