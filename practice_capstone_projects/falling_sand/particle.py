from colours import Colours
import random
import colorsys

def random_color(hue_range, saturation_range, value_range):
    hue = random.uniform(*hue_range)
    saturation = random.uniform(*saturation_range)
    value = random.uniform(*value_range)

    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

    return (int(r*255), int(g*255), int(b*255))

class SandParticle:
    def __init__(self):
        self.colour = random_color((0.1, 0.12), (0.5, 0.7), (0.6, 0.8))

    def update(self, grid, row, column):
        # 1. Fall straight down if empty
        if grid.is_cell_empty(row + 1, column):
            return (row + 1, column)

        # 2. Sink into water if present
        particle_below = grid.get_cell(row + 1, column)
        if isinstance(particle_below, WaterParticle):
            return (row + 1, column)  # Suggests swap (water should move up)

        # 3. Diagonal fall or sink
        offsets = [-1, 1]
        random.shuffle(offsets)

        for offset in offsets:
            new_col = column + offset

            # 3a. Fall diagonally if empty
            if grid.is_cell_empty(row + 1, new_col):
                return (row + 1, new_col)

            # 3b. Sink diagonally into water
            particle_diag = grid.get_cell(row + 1, new_col)
            if isinstance(particle_diag, WaterParticle):
                return (row + 1, new_col)

        # 4. No movement
        return (row, column)

class WaterParticle:
    def __init__(self):
        self.colour = random_color((0.55, 0.65), (0.6, 0.9), (0.8, 1.0))
        
        self.max_sliding_energy = 200
        self.sliding_energy = self.max_sliding_energy

    def update(self, grid, row, column):
        # 1. Try falling straight down
        if grid.is_cell_empty(row + 1, column):
            self.sliding_energy = self.max_sliding_energy  # Reset energy
            return (row + 1, column)

        # 2. Try diagonal fall (simulate natural flow)
        offsets = [-1, 1]
        random.shuffle(offsets)

        for offset in offsets:
            new_col = column + offset
            if grid.is_cell_empty(row + 1, new_col):
                self.sliding_energy = self.max_sliding_energy
                return (row + 1, new_col)

        # 3. Allow horizontal sliding if energy remains
        if self.sliding_energy > 0:
            for offset in offsets:
                new_col = column + offset
                if grid.is_cell_empty(row, new_col):
                    self.sliding_energy -= 1
                    return (row, new_col)

        # 4. Occasionally slide even when settled (simulate leveling)
        # This helps eliminate "clumps" and allows water to level out
        if random.random() < 0.1:  # 10% chance to drift left/right
            for offset in offsets:
                new_col = column + offset
                if grid.is_cell_empty(row, new_col):
                    return (row, new_col)

        # 5. No movement
        return (row, column)

class RockParticle:
    def __init__(self):
        self.colour = random_color((0.0, 0.1),(0.1, 0.3),(0.3, 0.5))
    
    def update(self, grid, row, column):
        return(row, column)
    
class StickySandParticle:
    def __init__(self):
        self.colour = random_color((0.13, 0.17), (0.6, 0.9), (0.3, 0.5))

    def update(self, grid, row, column):
        # 1. Fall straight down if empty
        if grid.is_cell_empty(row + 1, column):
            return (row + 1, column)
        
        # 2. Return same position if particle below is of the same type
        particle_below = grid.get_cell(row + 1, column)
        if isinstance(particle_below, StickySandParticle):
            return (row, column)

        # 3. Sink into water if present
        if isinstance(particle_below, WaterParticle):
            return (row + 1, column)  # Suggests swap (water should move up)
        

        # 4. Diagonal fall or sink
        offsets = [-1, 1]
        random.shuffle(offsets)

        for offset in offsets:
            new_col = column + offset

            # 3a. Fall diagonally if empty
            if grid.is_cell_empty(row + 1, new_col):
                return (row + 1, new_col)

            # 3b. Sink diagonally into water
            particle_diag = grid.get_cell(row + 1, new_col)
            if isinstance(particle_diag, WaterParticle):
                return (row + 1, new_col)

        # 5. No movement
        return (row, column)

class PixelParticle(SandParticle):
    def __init__(self, color):
        if not (isinstance(color, tuple) and len(color) == 3):
            raise ValueError("Color must be an RGB tuple, e.g., (255, 255, 0)")
        super().__init__()
        self.colour = color
