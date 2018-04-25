import app

def test_compound_interest():
    assert app.compound_interest(1000, 0.04, 100) == 50504.95
