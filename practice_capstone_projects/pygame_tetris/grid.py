from colours import Colours
import pygame

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.padding = 10
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colours = Colours.get_cell_colours()
        self.grid_line_size = 1

    def print_grid(self):
        for row in range(self.num_rosws):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()
    
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        else:
            return False

    def draw(self, screen):
        #"screen" is the screen where we want to draw in
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                #Square colour
                cell_value = self.grid[row][column]
                
                #Square size and position
                cell_rect = pygame.Rect(column*self.cell_size + self.grid_line_size + self.padding, 
                                        row*self.cell_size + self.grid_line_size + self.padding, 
                                        self.cell_size - self.grid_line_size, 
                                        self.cell_size - self.grid_line_size)
                
                #Draw square in pygame screen
                pygame.draw.rect(screen, self.colours[cell_value], cell_rect)
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        else:
            return False 

    def is_row_full(self, row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:            
                return False
        return True

    def clear_row(self, row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0
    
    def move_row_down(self, row, num_rows):
        for col in range(self.num_cols):
            self.grid[row+num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0
    
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    
    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0