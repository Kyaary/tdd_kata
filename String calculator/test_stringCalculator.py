def add(stringParameter):
    if not stringParameter:
        return "0"
    
def test_should_return_empty():
    assert add("") == "0" 

def test_should_return_sum():
    assert add("1,2")== "3"