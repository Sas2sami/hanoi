# Wieże Hanoi - porównanie algorytmów

Projekt zaliczeniowy z przedmiotu Sztuczna inteligencja_Sz_2025/2026_L_I1_N.

Celem projektu jest porównanie metod przeszukiwania przestrzeni stanów na przykładzie problemu Wież Hanoi.

W projekcie porównywane są trzy metody:

- DFS / brute force
- BFS
- BFS dwukierunkowe

Program sprawdza:

- liczbę ruchów,
- liczbę odwiedzonych stanów,
- czas działania algorytmu.

## Instalacja

Jeśli `uv` nie jest zainstalowane, można je zainstalować poleceniem:

```shell
pip install uv
```

Synchronizacja zależności:

```shell
uv sync
```


## Uruchomienie

```shell
uv run hanoi
```

## Testy

```shell
uv run pytest
```
## Sprawdzenie jakości kodu

```shell
uvx ruff check
```

## Przykładowy wynik

Po uruchomieniu program pyta o liczbę krążków:

```text
Podaj liczbę krążków: 3
```

Następnie wypisuje porównanie algorytmów, np.:

```text
PORÓWNANIE ALGORYTMÓW
Liczba krążków: 3
Optymalna liczba ruchów: 7

BFS
Liczba ruchów: 7
Liczba odwiedzonych stanów: 24
Czas działania: 0.00012345 s

DFS
Liczba ruchów: 13
Liczba odwiedzonych stanów: 13
Czas działania: 0.00009876 s

BFS dwukierunkowe
Liczba ruchów: 7
Liczba odwiedzonych stanów: ...
Czas działania: ...
```