from functions import is_positive

def test_soma():
    assert sum([2, 2, 6]) == 10

def test_ispositive():
    assert is_positive(5) is True
    assert is_positive(-1) is False