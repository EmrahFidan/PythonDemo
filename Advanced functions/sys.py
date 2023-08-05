import sys

def calculate_roots(a, b, c):
    """
    Calculates the roots of the quadratic equation ax^2 + bx + c = 0.

    Args:
        a (int): Coefficient of x^2.
        b (int): Coefficient of x.
        c (int): Constant term.

    Returns:
        tuple: A tuple containing two roots of the quadratic equation.
    """
    delta = b**2 - 4 * a * c

    if delta < 0:
        return None  # Return None for imaginary roots.
    else:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        return x1, x2

def main():
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])

        roots = calculate_roots(a, b, c)

        if roots is not None:
            print("Roots:", roots[0], roots[1])
        else:
            print("No real roots.")
    else:
        sys.stderr.write("Please provide three integer arguments a, b, and c.\n")
        sys.stderr.flush()

if __name__ == "__main__":
    main()
