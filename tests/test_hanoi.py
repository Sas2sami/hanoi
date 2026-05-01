from app.main import legalny_ruch


def test_legalny_ruch():
    stan = {
        "A": [3, 2, 1],
        "B": [],
        "C": []
    }
    assert not legalny_ruch(stan, "A", "C")

    stan = {"A": [1], 
            "B": [2], 
            "C": []}
    assert legalny_ruch(stan, "A", "B")
    assert not legalny_ruch(stan, "B", "A")
