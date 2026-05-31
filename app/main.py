from app.algorytmy import bfs, bfs_dwukierunkowe, dfs
from app.hanoi import stan

#Główna funkcja programu
def main():
    n = int(input("Podaj liczbę krążków: "))
    start, goal = stan(n)
    optimum = 2**n - 1

    print("\nPORÓWNANIE ALGORYTMÓW")
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

    visited_count, czas, liczba_ruchow = bfs_dwukierunkowe(start, goal)
    print("\nBFS dwukierunkowe")
    print("Liczba ruchów:", liczba_ruchow)
    print("Liczba odwiedzonych stanów:", visited_count)
    print("Czas działania:", f"{czas:.8f} s")

    path_bfs, visited_bfs, czas_bfs = bfs(start, goal)
    path_dfs, visited_dfs, czas_dfs = dfs(start, goal)
    visited_bi, czas_bi, ruchy_bi = bfs_dwukierunkowe(start, goal)

    wyniki = {
        "BFS": {
            "ruchy": len(path_bfs),
            "stany": visited_bfs,
            "czas": czas_bfs,
        },
        "DFS": {
            "ruchy": len(path_dfs),
            "stany": visited_dfs,
            "czas": czas_dfs,
        },
        "BFS dwukierunkowe": {
            "ruchy": ruchy_bi,
            "stany": visited_bi,
            "czas": czas_bi,
        },
    }

    najmniej_ruchow = min(wyniki, key=lambda algorytm: wyniki[algorytm]["ruchy"])
    najmniej_stanow = min(wyniki, key=lambda algorytm: wyniki[algorytm]["stany"])
    najkrotszy_czas = min(wyniki, key=lambda algorytm: wyniki[algorytm]["czas"])

    print("\nWNIOSEK")
    print("Najmniej ruchów wykonał:", najmniej_ruchow)
    print("Najmniej stanów odwiedził:", najmniej_stanow)
    print("Najkrótszy czas działania miał:", najkrotszy_czas)

    print("\nInterpretacja:")
    print("- Liczba ruchów pokazuje, czy rozwiązanie jest optymalne.")
    print("- Liczba odwiedzonych stanów pokazuje ilość pracy algorytmu.")
    print("- Czas działania pokazuje wydajność praktyczną.")