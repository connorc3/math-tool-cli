from sympy import Eq, linsolve, solve, simplify

def equations_equal(eq1: Eq, eq2: Eq) -> bool:
    # # Check if both are constants

    # symbols_set = list(eq1.free_symbols.union(eq2.free_symbols))

    # # Handle constant equations
    # if not symbols_set:
    #     return simplify(eq1.lhs - eq1.rhs) == simplify(eq2.lhs - eq2.rhs)
    
    # x = symbols_set[0]

    # sol1 = solve(eq1, x)
    # sol2 = solve(eq2, x)

    # return sol1 == sol2
    symbols_set = list(eq1.free_symbols.union(eq2.free_symbols))

    # Handle constants
    if not symbols_set:
        return simplify(eq1.lhs - eq1.rhs) == simplify(eq2.lhs - eq2.rhs)

    # Try using linsolve for linear systems
    try:
        sol1 = linsolve([eq1], symbols_set)
        sol2 = linsolve([eq2], symbols_set)
        return sol1 == sol2
    except Exception:
        # Fallback: check symbolic equivalence
        expr1 = eq1.lhs - eq1.rhs
        expr2 = eq2.lhs - eq2.rhs
        return simplify(expr1 - expr2) == 0

def find_first_error(equations: list[Eq]) -> int | None:
    for i in range(len(equations) - 1):
        if not equations_equal(equations[i], equations[i+1]):
            return i + 1
    return None


