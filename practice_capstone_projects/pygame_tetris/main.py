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
reserve_surface = title_font.render("Reserved:", True, Colours.white)
game_over_surface = title_font.render("GAME OVER", True, Colours.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
reserve_rect = pygame.Rect((320, 460, 170, 150))

#"blit" means "Block Image Transfer"

#-----GAME PARAMETERS-----
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 620
FPS = 60

MIN_TICK = 100     # fastest tick (ms)
MAX_TICK = 700     # slowest tick (ms)
MAX_SCORE = 10000  # score at which you reach max speed
SOFT_DROP_TICK = 50   # how fast to move down when holding DOWN key

current_tick = MAX_TICK

GAME_UPDATE = pygame.USEREVENT #Define event to be called every time block needs to move down

pygame.time.set_timer(GAME_UPDATE, current_tick) #Make the block move down every 400ms

#-----GAME INITIALIZATION-----
game = Game()

#Canvas size for now is 300px by 600px
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Python Tetris")

#game_grid.print_grid()
clock = pygame.time.Clock()

#-----FUNCTIONS----
def get_tick_interval(score):
    # Linearly map score (0 → MAX_SCORE) to tick (MAX_TICK → MIN_TICK)
    ratio = min(score / MAX_SCORE, 1)  # clamp to 1.0
    return int(MAX_TICK - (MAX_TICK - MIN_TICK) * ratio)

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
            elif event.key == pygame.K_LEFT and game.game_over == False:
                game.move_current_block_left()
            
            elif event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_current_block_right()
            
            elif event.key == pygame.K_UP and game.game_over == False:
                game.rotate_current_block()

            elif event.key == pygame.K_DOWN and game.game_over == False:
                if event.key == pygame.K_DOWN:
                    pygame.time.set_timer(GAME_UPDATE, SOFT_DROP_TICK)
            
            elif event.key == pygame.K_SPACE:
                game.switch_to_reserve_block()
                
        # When player releases DOWN, go back to normal
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pygame.time.set_timer(GAME_UPDATE, current_tick)
    
        #Only move block down every 200ms when GAME_UPDATE is triggered
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_current_block_down()
    
    #Update the block tick rate as the score increases
    new_tick = get_tick_interval(game.score)
    if new_tick != current_tick:
        current_tick = new_tick
        pygame.time.set_timer(GAME_UPDATE, current_tick)
        print(current_tick)


    #Draw screen (objects)
    screen.fill(Colours.orange)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (365, 180, 50, 50))
    screen.blit(reserve_surface, (335, 430, 50, 50))
    
    pygame.draw.rect(screen, Colours.dark_orange, score_rect, 0, 10)
    pygame.draw.rect(screen, Colours.dark_orange, next_rect, 0, 10)
    pygame.draw.rect(screen, Colours.dark_orange, reserve_rect, 0, 10)

    score_text = title_font.render(str(game.score), True, Colours.white)
    screen.blit(score_text, score_text.get_rect(center=score_rect.center))

    game.draw(screen)

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 500, 50, 50))
        
    pygame.display.update()

    #Tick pygame's clock so game can keep going
    clock.tick(FPS)


#NOTE: Origin is at top left corner in computers
