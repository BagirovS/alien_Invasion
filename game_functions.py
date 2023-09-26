import sys
import pygame

def check_events():
    #Process keystrokes and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update image on the screen and display new screen"""
    # After every iteration redraw the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Display the last screen
    pygame.display.flip()

