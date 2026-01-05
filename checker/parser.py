from sympy import Eq, sympify

def parse_equation(eq_str: str) -> Eq:
    if "=" not in eq_str:
        raise ValueError("Equation must contain '='")

    left, right = eq_str.split("=")
    return Eq(sympify(left), sympify(right))
