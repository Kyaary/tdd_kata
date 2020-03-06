def isBissextile(year):
    if year%400 == 0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    elif year%100==0 and year%400!=0:
        return False

def test_should_year_be_multiple_of_400():
    assert isBissextile(400) == True

def test_should_year_be_divisible_by_4_but_not_by_100():
    assert isBissextile(2008) == True

def test_should_year_be_divisible_by_100_but_not_by_400():
    assert isBissextile(1800) == False

