from aoc.utilities import load_data


def test_load_data(): 
    assert load_data(2019, 1)[0:5] == str(56583)