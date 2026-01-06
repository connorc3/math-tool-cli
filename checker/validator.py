from sympy import Eq, linsolve, solve, simplify

def equations_equal(prev: Eq, curr: Eq) -> bool:
    # Get all symbols
    symbols_set = list(prev.free_symbols.union(curr.free_symbols))

    # Handle constants
    if not symbols_set:
        return simplify(prev.lhs - prev.rhs) == simplify(curr.lhs - curr.rhs)

    if len(symbols_set) != 1:
        raise ValueError("Only single-variable equations supported here")

    x = symbols_set[0]

    # Solve each equation for x
    sol_prev = solve(prev, x)
    sol_curr = solve(curr, x)

    # Compare sets ignoring order
    return set(sol_prev) == set(sol_curr)

def find_first_error(equations: list[Eq]) -> int | None:
    for i in range(len(equations) - 1):
        if not equations_equal(equations[i], equations[i+1]):
            return i + 1
    return None


