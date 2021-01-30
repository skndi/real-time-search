import search_algorithms
from search_algorithms import best_first_search

def search(start, goal, map, h):
    return search_algorithms.best_first_search.search(start, goal, map, lambda x, y: x + y, lambda x, y: 1, h);


            

