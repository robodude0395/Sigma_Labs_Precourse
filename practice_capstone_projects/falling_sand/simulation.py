from grid import Grid
from particle import *
import pygame
import sys
import random

class Simulation:
    def __init__(self, _width, _height, _cell_size):
        self.grid = Grid(_width, _height, _cell_size)
        self.CELL_SIZE = _cell_size
        self.mode = "sand"
        self.brush_size = 1
        self.mouse_col = 0
        self.mouse_row = 0

    def draw(self, window):
        self.grid.draw_window(window)
        self.draw_brush(window)
    
    def add_particle(self, row, column):
        if random.random() < 0.35:
            if self.mode == "sand":
                self.grid.add_particle(row, column, SandParticle)
            elif self.mode == "water":
                self.grid.add_particle(row, column, WaterParticle)
            elif self.mode == "sticky":
                self.grid.add_particle(row, column, StickySandParticle)
        if self.mode == "rock":
                self.grid.add_particle(row, column, RockParticle)
        elif self.mode == "erase":
            self.grid.remove_particle(row, column)
        elif self.mode == "image_paste":
            self.grid.paste_image("example_images/leopard.png", self.mouse_row, self.mouse_col)

    def remove_particle(self, row, column):
        self.grid.remove_particle(row, column)

    def update(self):
        for row in range(self.grid.rows - 2, -1, -1):  # Bottom-up
            column_range = range(self.grid.columns) if row % 2 == 0 else reversed(range(self.grid.columns))

            for column in column_range:
                particle = self.grid.get_cell(row, column)

                if particle is None:
                    continue

                new_row, new_col = particle.update(self.grid, row, column)

                if (new_row, new_col) == (row, column):
                    continue  # No movement

                target_particle = self.grid.get_cell(new_row, new_col)

                # ⬇️ Simple Sand-Water Swap
                if isinstance(particle, SandParticle) and isinstance(target_particle, WaterParticle):
                    # Swap positions
                    self.grid.set_cell(row, column, target_particle)
                    self.grid.set_cell(new_row, new_col, particle)

                # Normal movement into empty cell
                elif target_particle is None:
                    self.grid.set_cell(new_row, new_col, particle)
                    self.grid.remove_particle(row, column)


    def restart(self):
        self.grid.clear()
    
    def handle_controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key(event)
            
            if event.type == pygame.MOUSEWHEEL:
                self.handle_scroll(event)
            
        self.handle_mouse()
        
    def handle_key(self, event):
        if event.key == pygame.K_SPACE:
            self.restart()
        
        elif event.key == pygame.K_1:
            print("Sand mode")
            self.mode = "sand"
        elif event.key == pygame.K_2:
            print("Water mode")
            self.mode = "water"
        elif event.key == pygame.K_3:
            print("Rock mode")
            self.mode = "rock"
        
        elif event.key == pygame.K_4:
            print("Sticky mode")
            self.mode = "sticky"

        elif event.key == pygame.K_5:
            print("Erase mode")
            self.mode = "erase"
        
        elif event.key == pygame.K_6:
            print("Image paste mode")
            self.mode = "image_paste"

        elif event.key == pygame.K_p:
            self.grid.set_pachinko_example()

    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed() #Get pressed buttons
        if buttons[0] == True: #Is left mouse button clicked
            pos = pygame.mouse.get_pos()
            row = pos[1] // self.CELL_SIZE
            col = pos[0] // self.CELL_SIZE
            self.apply_brush(row, col)
    
    def apply_brush(self, row, column):
        for r in range(self.brush_size):
            for c in range(self.brush_size):
                current_row = row + r
                current_column = column + c

                if self.mode == "erase":
                    self.grid.remove_particle(current_row, current_column)
                else:
                    self.add_particle(current_row, current_column)

    def handle_scroll(self, event):
        if event.y < 0:
            self.brush_size = min(self.brush_size + 1, 30)  # Scroll up
        elif event.y > 0:
            self.brush_size = max(self.brush_size - 1, 1)   # Scroll down
        #print(f"Brush size: {self.brush_size}")


    def draw_brush(self, window):
        mouse_pos = pygame.mouse.get_pos()
        self.mouse_col = mouse_pos[0] // self.CELL_SIZE
        self.mouse_row = mouse_pos[1] // self.CELL_SIZE

        brush_visual_size = self.brush_size * self.CELL_SIZE
        if self.mode == "rock":
            colour = (100, 100, 100)
        elif self.mode == "sand":
            colour = (185, 142, 66)
        elif self.mode == "erase":
            colour = (255, 105, 180)
        elif self.mode == "water":
            colour = (0, 0, 255)
        elif self.mode == "image_paste":
            colour = (255, 255, 0)
        elif self.mode == "sticky":
            colour = (255, 165, 0)
        else:
            colour = (255, 255, 255)
        
        pygame.draw.rect(window, colour, (self.mouse_col*self.CELL_SIZE, self.mouse_row*self.CELL_SIZE, brush_visual_size, brush_visual_size))