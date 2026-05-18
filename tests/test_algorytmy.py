from app.algorytmy import bfs, bfs_dwukierunkowe, dfs

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
    visited_count, duration, liczba_ruchow = bfs_dwukierunkowe(start, goal)
    assert visited_count > 0
    assert duration >= 0
    assert liczba_ruchow == 7