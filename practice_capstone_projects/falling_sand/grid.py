import pygame
from colours import Colours
from particle import *
import random
from PIL import Image

class Grid:
    def __init__(self, _width, _height, _cell_size):
        self.rows = _height//_cell_size
        self.columns = _width//_cell_size
        self.cell_size = _cell_size
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        self.grid_line_width = 0

    
    def draw_window(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                particle = self.cells[row][column]
                if particle != None:
                    cell_colour = particle.colour
                    pygame.draw.rect(window, cell_colour, (column * self.cell_size, row * self.cell_size, self.cell_size - self.grid_line_width, self.cell_size - self.grid_line_width))

    def add_particle(self, row, column, particle_type):
        if 0 <= row < self.rows and 0 <= column < self.columns and self.cells[row][column] == None:
            self.cells[row][column] = particle_type()
    
    def remove_particle(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = None
            
    def is_cell_empty(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            if self.cells[row][column] == None:
                return True
        return False
    
    def set_cell(self, row, column, particle):
        if not(0 <= row < self.rows and 0 <= column < self.columns):
            return
        self.cells[row][column] = particle
    
    def get_cell(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.cells[row][column]
        else:
            return None
    
    def clear(self):
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]
    
    def set_pachinko_example(self):
        start = self.columns // 2
        pin_map = []
        pin_map.append([0]*self.columns)
        pin_map[0][start] = 1
        
        last_row = pin_map[0][:]
        for i in range(0, (self.rows//4)):
            empty_row = [0]*self.columns
            new_row = empty_row.copy()
            
            for j in range(self.columns):
                if last_row[j] == 1:
                    left_offset = j - 1
                    right_offset = j + 1

                    if left_offset > 0:
                        new_row[left_offset] = 1
                    if right_offset < self.columns:
                        new_row[right_offset] = 1
            
            pin_map.append(empty_row)
            pin_map.append(new_row)
            last_row = new_row

        for r in range(len(pin_map)):
            for c in range(self.columns):
                if pin_map[r][c] == 1:
                    self.cells[r+2][c] = RockParticle()

    def paste_image(self, image_path, row_offset, col_offset):
        """
        Pastes an image onto the grid as PixelParticles,
        skipping fully transparent pixels.

        Args:
            image_path: Path to the input image file.
            row_offset: Vertical offset on the grid.
            col_offset: Horizontal offset on the grid.
        """
        # Load image with alpha channel
        image = Image.open(image_path).convert('RGBA')
        img_width, img_height = image.size

        for row in range(min(self.rows - row_offset, img_height)):
            for col in range(min(self.columns - col_offset, img_width)):
                r, g, b, a = image.getpixel((col, row))

                # Skip fully transparent pixels
                if a == 0:
                    continue

                # Create and place a PixelParticle
                particle = PixelParticle((r, g, b))
                self.set_cell(row + row_offset, col + col_offset, particle)

    
