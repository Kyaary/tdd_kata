def isBissextile(year):
    if year%400 == 0:
        return True
    if year%4==0:
        if year%100!=0:
            return True
    if year%100==0:
        if year%400!=0:
            return False
    if year%4!=0:
        return False

def test_should_year_be_multiple_of_400():
    assert isBissextile(400) == True

def test_should_year_be_divisible_by_4_but_not_by_100():
    assert isBissextile(2008) == True

def test_should_year_be_divisible_by_100_but_not_by_400():
    assert isBissextile(1800) == False

def test_should_year_be_divisible_by_4():
    assert isBissextile(5) == False