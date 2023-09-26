import sys
import pygame

def check_events(ship):
    #Process keystrokes and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
                # Move ship to right
                # ship.rect.centerx += 2


def update_screen(ai_settings, screen, ship):
    """Update image on the screen and display new screen"""
    # After every iteration redraw the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Display the last screen
    pygame.display.flip()

