#Implementacja algorytmów BFS, DFS i BFS dwukierunkowego dla problemu Hanoi
import time
from collections import deque
from app.hanoi import get_moves

#Algorytm BFS
def bfs(start, goal):
    start_time = time.perf_counter()
    queue = deque([(start, [])])
    visited = set()
    visited_count = 0

    while queue:
        state, path = queue.popleft()

        if state == goal:
            czas = time.perf_counter() - start_time
            return path, visited_count, czas

        if state in visited:
            continue

        visited.add(state)
        visited_count += 1

        for next_state in get_moves(state):
            queue.append((next_state, path + [next_state]))

    czas = time.perf_counter() - start_time
    return None, visited_count, czas

#Algorytm DFS
def dfs(start, goal):
    start_time = time.perf_counter()
    stack = [(start, [])]
    visited = set()
    visited_count = 0

    while stack:
        state, path = stack.pop()

        if state == goal:
            czas = time.perf_counter() - start_time
            return path, visited_count, czas

        if state in visited:
            continue

        visited.add(state)
        visited_count += 1

        for next_state in get_moves(state):
            stack.append((next_state, path + [next_state]))

    czas = time.perf_counter() - start_time
    return None, visited_count, czas

#Algorytm BFS dwukierunkowy
def bfs_dwukierunkowe(start, goal):
    start_time = time.perf_counter()

    queue_start = deque([(start, 0)])
    queue_goal = deque([(goal, 0)])

    visited_start = {start: 0}
    visited_goal = {goal: 0}

    visited_count = 0

    while queue_start and queue_goal:
        state_start, distance_start = queue_start.popleft()
        visited_count += 1

        if state_start in visited_goal:
            liczba_ruchow = distance_start + visited_goal[state_start]
            czas = time.perf_counter() - start_time
            return visited_count, czas, liczba_ruchow

        for next_state in get_moves(state_start):
            if next_state not in visited_start:
                visited_start[next_state] = distance_start + 1
                queue_start.append((next_state, distance_start + 1))

        state_goal, distance_goal = queue_goal.popleft()
        visited_count += 1

        if state_goal in visited_start:
            liczba_ruchow = distance_goal + visited_start[state_goal]
            czas = time.perf_counter() - start_time
            return visited_count, czas, liczba_ruchow

        for next_state in get_moves(state_goal):
            if next_state not in visited_goal:
                visited_goal[next_state] = distance_goal + 1
                queue_goal.append((next_state, distance_goal + 1))

    czas = time.perf_counter() - start_time
    return visited_count, czas, None