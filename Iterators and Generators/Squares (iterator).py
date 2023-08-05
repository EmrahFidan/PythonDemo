class Squares:
    def __init__(self, maximum):
        self.maximum = maximum
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= self.maximum:
            result = self.number ** 2
            self.number += 1
            return result
        else:
            self.number = 1
            raise StopIteration

squares = Squares(5)

# Using the squares iterator to iterate through the square numbers up to 5.
for square in squares:
    print(square)
