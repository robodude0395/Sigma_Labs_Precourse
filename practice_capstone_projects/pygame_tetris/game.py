from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()] #Reference all tetris blocks
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("sounds/clear.ogg")
        #Add a "placed block" sound

        #Load background music
        pygame.mixer.music.load("sounds/music_final.ogg")
        pygame.mixer.music.set_volume(0.05)  # volume between 0.0 and 1.0. Music I got was too loud.

        #Play background music forever
        pygame.mixer.music.play(-1)
    
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300

        elif lines_cleared == 3:
            self.score += 500
        
        elif lines_cleared == 4:
            self.score += 800
        
        self.score += move_down_points

    def get_random_block(self):
        if(len(self.blocks) == 0):
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        
        return block

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        
        #Offsets for specific blocks
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
        

    def move_current_block_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)
    
    def move_current_block_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_current_block_up(self):
        self.current_block.move(-1, 0)
        if self.block_inside() == False:
            self.current_block.move(1, 0)
    
    def move_current_block_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()
    
    def rotate_current_block(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotate()
        else:
            self.rotate_sound.play()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        
        #Update whole grid to include the block
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        cleared_rows = self.grid.clear_full_rows()

        if(cleared_rows > 0):
            self.clear_sound.play()
            self.update_score(cleared_rows, 0)

        if self.block_fits() == False:
            #GAME OVER
            self.game_over = True

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def reset(self):
        self.score = 0
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()] #Reference all tetris blocks
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()