from pygame.draw import rect
from pygame import Rect

class map(object):

    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells = []
        for x in range(0, int(self.width / self.cell_size)):
            self.cells.append(list())
            for y in range(0, int(self.height / self.cell_size)):
                self.cells[x].append(0)
   
    def render(self, win):
        counter_x = 0
        counter_y = 0
        for x in range(0, self.width, self.cell_size):
            for y in range(0, self.height, self.cell_size):
                rect(win, [x * self.cells[counter_x][counter_y] for x in (255, 255, 255)], Rect(x, y, self.cell_size, self.cell_size))
                counter_y += 1
            counter_y = 0
            counter_x += 1

    def get_neighbors(self, cell):
        neighbors = list()
        if(cell[0] > 0):
            if(not self.cells[cell[0] - 1][cell[1]]):
                neighbors.append((cell[0] - 1, cell[1]))
        if(cell[1] > 0):
            if(not self.cells[cell[0]][cell[1] - 1]):
                neighbors.append((cell[0], cell[1] - 1))
        if(cell[0] < len(self.cells) - 1):
            if(not self.cells[cell[0] + 1][cell[1]]):
                neighbors.append((cell[0] + 1, cell[1]))
        if(cell[1] < len(self.cells[0]) - 1):
            if(not self.cells[cell[0]][cell[1] + 1]):
                neighbors.append((cell[0], cell[1] + 1))
        return neighbors

    def change_cell(self, position):
        self.cells[int(position[0] / self.cell_size)][int(position[1] / self.cell_size)] = 1

    def get_map():
        return self.cells