from sympy import Eq, simplify, diff, integrate

SUPPORTED_OPS = {"differentiate", "integrate", "simplify"}

def validate_calculus_step(prev: Eq, curr: Eq, operation: str) -> bool:
    if operation not in SUPPORTED_OPS:
        raise ValueError("Unsupported operation")
    
    x1 = list(prev.free_symbols)
    

    if operation == "differentiate":
        expected = diff(prev)
    elif operation == "integrate":
        expected = integrate(prev)
    elif operation == "simplify":
        expected = simplify(prev)
    
    return simplify(expected - curr) == 0
