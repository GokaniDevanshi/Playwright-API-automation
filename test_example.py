# def test_function():
#     print("This is a pytest")
def add(a,b):
    return a+b
def test_add():
    assert add(2,3)==6
