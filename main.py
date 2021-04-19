from time import time
from depth_first_search import dfs
from eight_puzzle import Puzzle

initial_state = [2, 8, 3,
                 1, 6, 4,
                 7, 0, 5]

Puzzle.num_of_instances = 0
t0 = time()
solution = dfs(initial_state)
t1 = time() - t0
print('Solution:', solution)
print('space:', Puzzle.num_of_instances)
print('time:', t1, "seconds")
print()
