import pygame
import map
import agent
import time

def draw_map(win, cell_size, map_width, map_height, color):
    for x in range(0, map_height, cell_size):
        for y in range(0, map_width, cell_size):
            pygame.draw.rect(win, color, pygame.Rect(y, x, cell_size, cell_size), 1)

def render():
    win.fill((0, 0, 0))
    area.render(win)
    ag.render(win)
    pygame.display.update()
    

def update():
    if(mark):
        area.change_cell(pygame.mouse.get_pos())
    if(not paused):
        ag.update(area)

width = 500
height = 500
cell_size = 10
pygame.init()
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
color = (255, 255, 255)
area = map.map(width, height, cell_size)
mark = False
ag = agent.agent(cell_size, (0, 255, 0), [0, 100], lambda lhs, rhs: abs(lhs[0] - rhs[0]) + abs(lhs[1] - rhs[1]))
ag.set_goal((490, 490))
paused = True

while True:
    dt = clock.get_time()

    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT: 
            pygame.quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            mark = True
        elif ev.type == pygame.MOUSEBUTTONUP:
            mark = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                paused = not paused
    render()
    update()
    clock.tick(60)