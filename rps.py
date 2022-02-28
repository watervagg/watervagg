# To install pygame, type 'pip install pygame' in the 
# windows powershell or the os terminal

# To create a blank screen as a setup for a game, use:
import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

FPS = 30 # How many times the screen will update per second

screen_width = 600 # How wide the window will be
screen_height = 600 # how high the window will be

screen = pygame.display.set_mode((screen_width, screen_height)) # creates the screen

while True:
    clock.tick(FPS) # updates the screen, the amount of times it does so depends on the FPS
    for event in pygame.event.get(): # Allows you to add various events
        if event.type == pygame.QUIT: # Allows the user to exit using the X button
            pygame.quit()
            sys.exit()