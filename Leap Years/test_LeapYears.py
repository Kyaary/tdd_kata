def isBissextile(year):
    if year%400 == 0:
        return True

def test_year_is_multiple_of_400():
    assert isBissextile(400) == True

def test_year_is_divisible_by_4_but_not_by_100():
    assert isBissextile(2008) == True