import sys
from checker.parser import parse_equation
from checker.validator import find_first_error
from checker.feedback import basic_feedback

def main():
    print("Enter equations step-by-step. Empty line to finish.\n")

    equations = []
    while True:
        line = input("> ").strip()
        if not line:
            break
        try:
            equations.append(parse_equation(line))
        except Exception as e:
            print(f"Invalid equation: {e}")
            return
    
    if len(equations) < 2:
        print("Need at least two steps.")
        return

    error_step = find_first_error(equations)

    if error_step is None:
        print("\nAll steps are valid!")
    else:
        print("\nError detected.")
        print(basic_feedback(error_step))

if __name__ == "__main__":
    main()
