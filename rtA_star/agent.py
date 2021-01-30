import queue
import sys
from pygame.draw import rect
from pygame import Rect
from copy import deepcopy
from collections import defaultdict

class agent(object):
    
    def __init__(self, cell_size, color, map_position, h):
        self.size = cell_size
        self.color = color
        self.remembered_states = defaultdict(lambda: 0)
        self.map_position = map_position 
        self.position = deepcopy(map_position)
        self.position[0] = int(self.position[0] / 10)
        self.position[1] = int(self.position[1] / 10)
        self.h = h
        self.goal = deepcopy(self.map_position)
        self.goal_color = (255, 0, 0)

    def update(self, map):
        if(self.position != self.goal):
            min = sys.maxsize
            best_choice = tuple()
            for neighbor in map.get_neighbors(self.position):
                if(self.remembered_states[tuple(neighbor)]):
                    weight = self.remembered_states[tuple(neighbor)] + 1
                else: weight = self.h(neighbor, self.goal) + 1
                if weight < min:
                    print(weight)
                    min = weight
                    best_choice = neighbor
            self.remembered_states[tuple(self.position)] = min
            self.move_to(best_choice)

    def move_to(self, new_position):
        dx = new_position[0] - self.position[0]
        dy = new_position[1] - self.position[1]
        self.position[0] += dx
        self.position[1] += dy
        self.map_position[0] = int(self.position[0]) * self.size
        self.map_position[1] = int(self.position[1]) * self.size

    def render(self, win):
        rect(win, self.goal_color, Rect(self.goal[0] * 10, self.goal[1] * 10, self.size, self.size))
        rect(win, self.color, Rect(self.map_position[0], self.map_position[1], self.size, self.size))

    def set_goal(self, goal):
        self.goal[0] = goal[0] / self.size
        self.goal[1] = goal[1] / self.size