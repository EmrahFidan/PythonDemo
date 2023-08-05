def find_pythagorean_triples(limit=100):
    """
    Find Pythagorean triples (a, b, c) where a, b, and c are positive integers,
    and a, b are both less than or equal to the given limit (default: 100).
    """
    pythagorean_triples = []
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            c_square = a ** 2 + b ** 2
            c = int(c_square ** 0.5)

            if c <= limit and c_square == c ** 2:
                pythagorean_triples.append((a, b, c))

    return pythagorean_triples

def main():
    pythagorean_triples = find_pythagorean_triples()

    for triple in pythagorean_triples:
        print(triple)

if __name__ == "__main__":
    main()
