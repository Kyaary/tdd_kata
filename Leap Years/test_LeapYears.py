def isBissextile(x):
    if x%400 == 0:
        return True

def test_year_is_multiple_of_400():
    assert isBissextile(400) == True