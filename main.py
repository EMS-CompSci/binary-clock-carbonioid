import pygame
from clock import Clock
from display import ClockDisplay

pygame.init()

pygame.display.set_caption('Title')
surface = pygame.display.set_mode((800, 600))

clock = Clock()
displayer = ClockDisplay(surface)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    surface.fill(pygame.Color('#ffffff'))

    displayer.display_clock(clock.time_as_binary())

    pygame.display.update()