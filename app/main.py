stan = {
    "A": [3, 2, 1],
    "B": [],
    "C": []
}
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

if __name__ == "__main__":
    print(f"Stan początkowy: {stan}")
    hanoi(len(stan["A"]), "A", "C", "B", stan)
    print(f"Stan końcowy: {stan}")
