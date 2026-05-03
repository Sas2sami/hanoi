
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

def legalne_ruchy(stan,start,cel):
    if len(stan[start]) == 0:
        return False
    if len(stan[cel]) == 0:
        return True
    return stan[start][-1] < stan[cel][-1]

def wykonaj_ruch(stan,start,cel):
    if legalne_ruchy(stan,start,cel):
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





