from src.math_operation import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(10,5) == 15
    
def test_sub():
    assert sub(7,5) == 2
    assert sub(13,5)== 8
