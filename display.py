import pygame

class ClockDisplay:
    def __init__(self, surface):
        self.surface = surface

        self.dot_padding = 15
        self.dot_radius = 50

        self.clock_padding = 50

        self.clock_start = (50, 50) # Left corner

    def display_clock(self, values):
        """Take values from Clock class as defined in Clock.time_as_binary() and display them as a binary clock on
        the pygame.surface.Surface object `self.surface`

        Args:
            values (List[List[List[int], List[int]]]): time split into 6 binary sections
            surface (pygame.surface.Surface): the surface to draw on
        """

        current_corner = list(self.clock_start)
        for columns in values:
            for column in columns: # columns = [tens, units]
                # Move down y as dots are drawn
                y = current_corner[1]
                for value in column:
                    pygame.draw.circle(self.surface, (0, 0, 0), (current_corner[0], y), self.dot_radius, abs(1-value))

                    y += self.dot_padding + self.dot_radius*2
                
                # Move across in x by padding and radius to start new column
                current_corner[0] += self.dot_padding + self.dot_radius*2

            current_corner[0] += self.clock_padding # move along in x by padding to start new "area" (e.g. hour/min/second)

    