from calculator import divide

# Example 4: Using side_effect to Simulate Different Behaviors


def test_divide_with_side_effect(mocker):
    mocker.patch('calculator.divide', side_effect=[5, ZeroDivisionError("division by zero")])
    
    # First call returns 5
    assert divide(10, 2) == 5
    
    # Second call raises ZeroDivisionError
    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        assert str(e) == "division by zero"
