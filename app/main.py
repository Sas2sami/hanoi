stan = {
    "A": [3, 2, 1],
    "B": [],
    "C": []
}
def hanoi(n, start, cel, pomocniczy):
    if n == 1:
        print(f"Przenieś dysk 1 z {start} do {cel}")
    else:
        hanoi(n - 1, start, pomocniczy, cel)
        print(f"Przenieś dysk {n} z {start} do {cel}")
        hanoi(n - 1, pomocniczy, cel, start)

def legalne_ruch(stan,start,cel):
    if len(stan[start]) == 0:
        return False
    if len(stan[cel]) == 0:
        return True
    return stan[start][-1] < stan[cel][-1]

hanoi(3, "A", "C", "B")
print(stan)
