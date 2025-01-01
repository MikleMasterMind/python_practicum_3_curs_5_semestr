from prog1 import solve

def test1():
    assert solve(1, -5, 4) == [-2.0, -1.0, 1.0, 2.0]
    
def test2():
    assert solve(0, 2, -32) == [-4.0, 4.0]

def test3():
    assert solve(0, 2, 32) == [0]

def test4():
    assert solve(0, 0, 2) == [0]

def test5():
    assert solve(0, 0, 0) == [-1]

def test6():
    assert solve(12, 13, 0) == [0]
    
def test7():
    assert solve(1, 7, 12) == [0]
    
def test8():
    assert solve(1, -1, -12) == [-2.0, 2.0]
    
def test9():
    assert solve(1, -1, 0) == [-1.0, 0, 1.0]


    