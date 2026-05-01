from app.main import legalny_ruch


def test_legalny_ruch():
    stan = {
        "A": [3, 2, 1],
        "B": [],
        "C": []
    }
    assert legalny_ruch(stan, "A", "B") == True
    assert legalny_ruch(stan, "C", "A") == False

    stan = {"A": [1], 
            "B": [2], 
            "C": []}
    assert legalny_ruch(stan, "A", "B") == True  
    assert legalny_ruch(stan, "B", "A") == False

