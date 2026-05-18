from app.main import bfs, bfs_dwukierunkowe, dfs, hanoi, legalne_ruchy


def test_legalne_ruchy():
    stan = {
        "A": [3, 2],
        "B": [],
        "C": [1]
    }
    assert not legalne_ruchy(stan, "A", "C")

    stan = {"A": [1], 
            "B": [3,2], 
            "C": []}
    assert legalne_ruchy(stan, "A", "B")
    assert not legalne_ruchy(stan, "B", "A")

    stan = {"A": [], 
            "B": [3, 2, 1], 
            "C": []}
    assert not legalne_ruchy(stan, "A", "B")

def test_hanoi():
    stan = {
        "A": [3, 2, 1],
        "B": [],
        "C": []
    }
    hanoi(len(stan["A"]), "A", "C", "B", stan)
    assert stan == {
        "A": [],
        "B": [],
        "C": [3, 2, 1]
        }

def test_bfs():
    start = ((3, 2, 1), (), ())
    goal = ((), (), (3, 2, 1))
    path, visited_count, duration = bfs(start, goal)
    assert len(path) == 7
    assert path[-1] == goal
    assert visited_count > 0
    assert duration >= 0

def test_dfs():
    start = ((3, 2, 1), (), ())
    goal = ((), (), (3, 2, 1))
    path, visited_count, duration = dfs(start, goal)
    assert path[-1] == goal
    assert len(path) >= 7
    assert visited_count > 0
    assert duration >= 0

def test_bfs_dwukierunkowe():
    start = ((3, 2, 1), (), ())
    goal = ((), (), (3, 2, 1))
    visited_count, duration = bfs_dwukierunkowe(start, goal)
    assert visited_count > 0
    assert duration >= 0