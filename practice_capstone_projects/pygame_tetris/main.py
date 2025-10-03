import pygame
import sys
from grid import Grid
from colours import Colours
from blocks import *
from game import Game

pygame.init()

title_font = pygame.font.Font(None, 40) #Use default font
score_surface = title_font.render("Score: ", True, Colours.white)
next_surface = title_font.render("Next:", True, Colours.white)
game_over_surface = title_font.render("GAME OVER", True, Colours.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

#"blit" means "Block Image Transfer"

#-----GAME PARAMETERS-----
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 620
FPS = 60

GAME_UPDATE = pygame.USEREVENT #Define event to be called every time block needs to move down
pygame.time.set_timer(GAME_UPDATE, 400) #Make the block move down every 200ms

#-----COLOURS-----
dark_blue = (44, 44, 127)

#-----GAME INITIALIZATION-----
game = Game()

#Canvas size for now is 300px by 600px
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Python Tetris")

#game_grid.print_grid()
clock = pygame.time.Clock()

#-----GAME LOOP----

#WHAT HAPPENS:
#   Event handling
#   Collision detections
#   Update positions
#   Draw Objects

while True:
    #Event handling
    for event in pygame.event.get(): #Go through all the events pygame registered
        #If the user closes the game, then exit and shut down the game.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #Handle key input
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_current_block_left()
            
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_current_block_right()
            
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate_current_block()

            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_current_block_down()
                game.update_score(0, 1)
        
        #Only move block down every 200ms when GAME_UPDATE is triggered
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_current_block_down()
    
    #Draw screen (objects)
    screen.fill(Colours.orange)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (365, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    
    pygame.draw.rect(screen, Colours.dark_orange, score_rect, 0, 10)
    pygame.draw.rect(screen, Colours.dark_orange, next_rect, 0, 10)

    score_text = title_font.render(str(game.score), True, Colours.white)
    screen.blit(score_text, score_text.get_rect(center=score_rect.center))

    game.draw(screen)
    pygame.display.update()

    #Tick pygame's clock so game can keep going
    clock.tick(FPS)


#NOTE: Origin is at top left corner in computers
