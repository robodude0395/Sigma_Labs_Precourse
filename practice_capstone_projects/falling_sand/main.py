import pygame
import sys
from simulation import Simulation
from colours import Colours

#-----DEFINITIONS-----
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 3 
FPS = 240 #Simulation frames per second (more frames=faster simulation)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))#Create a display surface
pygame.display.set_caption("Falling Sand")
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

#-----MAIN PROGRAM-----
while True:
    #1.Handle events
    simulation.handle_controls()

    #2.Update grid state
    simulation.update()

    #3.Drawing updated grid
    window.fill(Colours.black)
    simulation.draw(window)

    pygame.display.flip() #.flip is used to draw sim objects
    clock.tick(FPS)