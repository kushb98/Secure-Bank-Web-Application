import pytest
from MyCalc import MyCalc

def test_addition():
    calc = MyCalc()
    assert calc.add(3, 4) == 7
    assert calc.add(10.25, 11.75) == 22
    assert calc.add(-11, -44) == -55

def test_subtraction():
    calc = MyCalc()
    assert calc.sub(10, 5) == 5
    assert calc.sub(10, 15) == -5
    assert calc.sub(-10, 5) == -15

def test_multiplication():
    calc = MyCalc()
    assert calc.mul(10, 5) == 50
    assert calc.mul(10, -15) == -150
    assert calc.mul(-10, -5) == 50

def test_division():
    calc = MyCalc()
    assert calc.div(10, 5) == 2
    assert calc.div(15, -3) == -5
    assert calc.div(-10, -5) == 2

def test_division_by_zero():
    calc = MyCalc()
    # with pytest.raises(ZeroDivisionError):
    assert calc.div(5, 0) == None

def test_add_to_answer():
    calc = MyCalc()
    ans = 5
    assert calc.add(ans, 3) == 8
    assert calc.add(ans, -2) == 3
    assert calc.add(ans, 0) == 5

def test_sub_from_answer():
    calc = MyCalc()
    ans = 15
    assert calc.sub(ans, 3) == 12
    assert calc.sub(ans, -2) == 17
    assert calc.sub(ans, 0) == 15

def test_mul_to_answer():
    calc = MyCalc()
    ans = 9
    assert calc.mul(ans, 3) == 27
    assert calc.mul(ans, -2) == -18
    assert calc.mul(ans, 0) == 0

def test_div_answer():
    calc = MyCalc()
    ans = 27
    assert calc.div(ans, 3) == 9
    assert calc.div(ans, -2) == -13.5
    assert calc.div(ans, 27) == 1   

def test_div_answer_by_zero():
    calc = MyCalc()
    ans = 10
    assert calc.div(ans, 0) == None