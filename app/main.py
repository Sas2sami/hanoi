def hanoi(n, start, cel, pomocniczy):
    if n == 1:
        print(f"Przenieś dysk 1 z {start} do {cel}")
    else:
        hanoi(n - 1, start, pomocniczy, cel)
        print(f"Przenieś dysk {n} z {start} do {cel}")
        hanoi(n - 1, pomocniczy, cel, start)

hanoi(3, 'A', 'C', 'B')