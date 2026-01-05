from checker.parser import parse_equation
from checker.validator import find_first_error

def test_valid_solution():
    equations = [
        parse_equation("2*x + 3 = 7"),
        parse_equation("2*x = 4"),
        parse_equation("x = 2"),
    ]

    assert find_first_error(equations) is None

def test_invalid_solution():
    equations = [
        parse_equation("2*x + 3 = 7"),
        parse_equation("2*x = 5"),
        parse_equation("x = 2"),
    ]

    assert find_first_error(equations) == 1
