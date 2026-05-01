from app.main import hanoi, legalne_ruchy


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

