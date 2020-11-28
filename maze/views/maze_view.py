import pygame
import pygame.locals


class MazeView:

    def build_screen(self):
        # Screen is 800 x 700 pixels
        pygame.init()
        window = pygame.display.set_mode((800, 700))
        window.set_colorkey((255, 255, 255))
        return window

    # def display_result(self):
    #     # Screen is 800 x 700 pixels
    #     pygame.init()
    #     screen = pygame.display.set_mode((500, 500))
    #     screen.set_colorkey((255, 255, 255))

def display(self):
    # to display the map using print the all row string
    for line in self._map:
        # for each line in the nested list
        row_string = ''
        row_string = row_string.join(line)
        print(row_string)
