from colours import Colours
import pygame
from position import Position

class Block:
    def __init__(self, _id):
        self.id = _id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colours = Colours.get_cell_colours()
        self.col_pos = 0
        self.row_pos = 0

    def move(self, rows, cols): #Move block by x rows and y columns
        self.col_pos += cols
        self.row_pos += rows
    
    def rotate(self):
        self.rotation_state = (self.rotation_state+1)%4
    
    def undo_rotate(self):
        self.rotation_state = (self.rotation_state-1)%4

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved = []
        for position in tiles:
            position = Position(position.row + self.row_pos, 
                                position.column + self.col_pos)
            moved.append(position)
        return moved

    def draw(self, screen, offsetx=0, offsety=0):
        tiles = self.get_cell_positions()

        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + offsetx,
                                    tile.row * self.cell_size + offsety,
                                    self.cell_size - 1,
                                    self.cell_size - 1)
            pygame.draw.rect(screen, self.colours[self.id], tile_rect)