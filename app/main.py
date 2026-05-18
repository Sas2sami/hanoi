import time
from collections import deque

stan = {
    "A": [3, 2, 1],
    "B": [],
    "C": []
}
start = ((3, 2, 1), (), ())
goal = ((), (), (3, 2, 1))

def hanoi(n, start, cel, pomocniczy, stan):
    if n == 1:
        wykonaj_ruch(stan, start, cel)
    else:
        hanoi(n - 1, start, pomocniczy, cel, stan)
        wykonaj_ruch(stan, start, cel)
        hanoi(n - 1, pomocniczy, cel, start, stan)

def legalne_ruchy(stan, start, cel):
    if len(stan[start]) == 0:
        return False
    if len(stan[cel]) == 0:
        return True
    return stan[start][-1] < stan[cel][-1]

def wykonaj_ruch(stan, start, cel):
    if legalne_ruchy(stan, start, cel):
        dysk = stan[start].pop()
        stan[cel].append(dysk)
    else:
        print("Nielegalny ruch")

def get_moves(state):
    moves = []
    n = len(state)

    for i in range(n): 
        if not state[i]:
            continue
        disk = state[i][-1] 
        for j in range(n):
            if i == j:
                continue
            if not state[j] or state[j][-1] > disk:
                new_state = [list(rod) for rod in state]
                new_state[j].append(new_state[i].pop())
                moves.append(tuple(tuple(rod) for rod in new_state))
    return moves

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

def bfs_dwukierunkowe(start, goal):
    start_time = time.perf_counter()
    queue_start = deque([start])
    queue_goal = deque([goal])
    visited_start = {start}
    visited_goal = {goal}
    visited_count = 0

    while queue_start and queue_goal:
        state_start = queue_start.popleft()
        visited_count += 1

        if state_start in visited_goal:
            czas = time.perf_counter() - start_time
            return visited_count, czas

        for next_state in get_moves(state_start):
            if next_state not in visited_start:
                visited_start.add(next_state)
                queue_start.append(next_state)

        state_goal = queue_goal.popleft()
        visited_count += 1

        if state_goal in visited_start:
            czas = time.perf_counter() - start_time
            return visited_count, czas

        for next_state in get_moves(state_goal):
            if next_state not in visited_goal:
                visited_goal.add(next_state)
                queue_goal.append(next_state)

    czas = time.perf_counter() - start_time
    return visited_count, czas

if __name__ == "__main__":
    n = len(start[0])
    optimum = 2**n - 1

    print("PORÓWNANIE ALGORYTMÓW")
    print("Liczba krążków:", n)
    print("Optymalna liczba ruchów:", optimum, "\n")

    path, visited_count, czas = bfs(start, goal)
    print("BFS")
    print("Liczba ruchów:", len(path))
    print("Liczba odwiedzonych stanów:", visited_count)
    print("Czas działania:", f"{czas:.8f} s")

    path, visited_count, czas = dfs(start, goal)
    print("\nDFS")
    print("Liczba ruchów:", len(path))
    print("Liczba odwiedzonych stanów:", visited_count)
    print("Czas działania:", f"{czas:.8f} s")

    visited_count, czas = bfs_dwukierunkowe(start, goal)
    print("\nBFS dwukierunkowe")
    print("Liczba odwiedzonych stanów:", visited_count)
    print("Czas działania:", f"{czas:.8f} s")


