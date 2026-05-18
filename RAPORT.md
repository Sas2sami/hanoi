# Raport — Wieże Hanoi

## 1. Opis zastosowanych algorytmów

W projekcie zastosowano trzy metody przeszukiwania przestrzeni stanów do rozwiązania problemu Wież Hanoi:

- DFS / brute force
- BFS
- BFS dwukierunkowe

Celem było porównanie algorytmów pod względem:

- liczby wykonanych ruchów,
- liczby odwiedzonych stanów,
- czasu działania.

Problem Wież Hanoi został potraktowany jako problem przeszukiwania przestrzeni stanów. Każdy stan oznacza aktualne rozmieszczenie krążków na trzech słupkach, a każda akcja oznacza jeden poprawny ruch krążka.

---

## 2. DFS / brute force

DFS przeszukuje przestrzeń stanów w głąb.

Algorytm:

- rozpoczyna od stanu początkowego,
- generuje możliwe kolejne ruchy,
- przechodzi jak najdalej jedną ścieżką,
- kończy działanie po znalezieniu stanu docelowego.

DFS został użyty jako prosta metoda bazowa. Pozwala sprawdzić, jak działa podejście bez gwarancji znalezienia najlepszego rozwiązania.
Wynik DFS może być poprawny, ale nie musi mieć minimalnej liczby ruchów.

---

## 3. BFS

BFS przeszukuje przestrzeń stanów poziomami.

Algorytm:

- najpierw sprawdza wszystkie stany osiągalne w 1 ruchu,
- potem w 2 ruchach,
- następnie w 3 ruchach itd.,
- kończy działanie po znalezieniu stanu docelowego.

BFS został wybrany, ponieważ w problemie Wież Hanoi każdy ruch ma taki sam koszt. Dzięki temu BFS znajduje rozwiązanie o minimalnej liczbie ruchów.

Dla `n` krążków optymalna liczba ruchów wynosi:


```text
2^n - 1
```

---

## 4. BFS dwukierunkowe

BFS dwukierunkowe jest rozszerzeniem zwykłego BFS.

Algorytm:

- rozpoczyna przeszukiwanie od stanu początkowego,
- jednocześnie rozpoczyna przeszukiwanie od stanu końcowego,
- kończy działanie, gdy oba przeszukiwania spotkają się w tym samym stanie.

Metoda ta została wybrana jako algorytm spoza podstawowego zakresu zajęć. Jej celem jest ograniczenie liczby odwiedzanych stanów w porównaniu do klasycznego BFS.

W projekcie BFS dwukierunkowe zwraca:

- liczbę ruchów,
- liczbę odwiedzonych stanów,
- czas działania.

---

## 5. Dane wejściowe

Dane są generowane automatycznie na podstawie liczby krążków podanej przez użytkownika.

Przykład dla 3 krążków:

```python
start = ((3, 2, 1), (), ())
goal = ((), (), (3, 2, 1))
```

Stan początkowy oznacza, że wszystkie krążki znajdują się na pierwszym słupku.
Stan końcowy oznacza, że wszystkie krążki mają zostać przeniesione na trzeci słupek.
Program pozwala podać dowolną liczbę krążków, np.:

```text
Podaj liczbę krążków: 3
```

---

## 6. Parametry porównania

W projekcie porównywane są trzy wartości:

### Liczba ruchów

Liczba ruchów pokazuje, ile kroków wykonał algorytm, aby dojść do rozwiązania.
Jest to najważniejsze kryterium jakości rozwiązania.
Jeżeli liczba ruchów jest równa:

```text
2^n - 1
```

to rozwiązanie jest optymalne.

### Liczba odwiedzonych stanów

Liczba odwiedzonych stanów pokazuje, ile różnych układów krążków algorytm musiał sprawdzić podczas szukania rozwiązania.
Mniejsza liczba odwiedzonych stanów oznacza, że algorytm wykonał mniej pracy.

### Czas działania

Czas działania pokazuje, jak szybko algorytm znalazł rozwiązanie.
Dla małej liczby krążków czas może być bardzo krótki, dlatego nie powinien być jedynym kryterium oceny.

---

## 7. Testy

Przeprowadzono testy automatyczne sprawdzające poprawność działania najważniejszych funkcji.

Testy obejmują:

- sprawdzanie legalności ruchów,
- poprawność klasycznego rozwiązania Hanoi,
- działanie BFS,
- działanie DFS,
- działanie BFS dwukierunkowego.

Dla 3 krążków sprawdzono, czy BFS znajduje rozwiązanie o długości 7 ruchów, czyli zgodne z wartością optymalną:

```text
2^3 - 1 = 7
```

Testy uruchamiane są poleceniem:

```shell
uv run pytest
```

---

## 8. Przykładowe wyniki

Dla 3 krążków optymalna liczba ruchów wynosi:

```text
7
```

Przykładowy wynik programu:

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

Czas działania może się różnić w zależności od komputera.

---

## 9. Wyniki i wnioski

Na podstawie działania programu można zauważyć, że:

- BFS znajduje rozwiązanie optymalne, ponieważ liczba ruchów jest zgodna ze wzorem `2^n - 1`.
- DFS znajduje rozwiązanie poprawne, ale nie zawsze optymalne.
- DFS może odwiedzić mniej stanów, ale nie oznacza to, że wynik jest lepszy.
- BFS odwiedza więcej stanów, ale daje gwarancję znalezienia minimalnej liczby ruchów.
- BFS dwukierunkowe również znajduje rozwiązanie optymalne.
- BFS dwukierunkowe ogranicza przeszukiwanie, ponieważ działa jednocześnie od stanu początkowego i końcowego.
- Liczba ruchów pokazuje jakość rozwiązania.
- Liczba odwiedzonych stanów pokazuje ilość pracy wykonanej przez algorytm.
- Czas działania pokazuje wydajność praktyczną, ale dla małej liczby krążków różnice czasowe są bardzo małe.

Najlepszym algorytmem pod względem liczby ruchów jest BFS oraz BFS dwukierunkowe, ponieważ znajdują rozwiązanie optymalne.
DFS jest najprostszą metodą, ale nie gwarantuje najlepszego rozwiązania.
BFS dwukierunkowe jest dobrym rozszerzeniem BFS, ponieważ zachowuje optymalność i może zmniejszyć liczbę odwiedzanych stanów.

---

## 10. Podsumowanie

Projekt pokazuje różnice między prostym przeszukiwaniem w głąb, klasycznym BFS oraz BFS dwukierunkowym.
Najważniejszy wniosek jest taki, że nie każdy algorytm, który szybko znajduje rozwiązanie, znajduje rozwiązanie najlepsze.
W problemie Wież Hanoi najważniejsza jest minimalna liczba ruchów, dlatego BFS i BFS dwukierunkowe wypadają najlepiej pod względem jakości rozwiązania.
