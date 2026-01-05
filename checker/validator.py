from sympy import Eq, simplify

def equations_equal(eq1: Eq, eq2: Eq) -> bool:
    diff1 = simplify(eq1.lhs, eq1.rhs)
    diff2 = simplify(eq2.lhs, eq2.rhs)
    return simplify(diff1, diff2) == 0

def find_first_error(equations: list[Eq]) -> int | None:
    for i in range(len(equations) - 1):
        if not equations_equal(equations[i], equations[i+1]):
            return i + 1
    return None


