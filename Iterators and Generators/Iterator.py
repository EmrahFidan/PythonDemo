class PowerOf3:
    def __init__(self, max=0):
        """
        Initializes the PowerOf3 iterable.

        Args:
            max (int): The maximum power of 3 to generate. Default is 0.
        """
        self.max = max
        self.power = 0

    def __iter__(self):
        """
        Makes this class an iterator.

        Returns:
            PowerOf3: It returns itself, as this class is both an iterable and an iterator.
        """
        return self

    def __next__(self):
        """
        Gets the next power of 3.

        Returns:
            int: The next power of 3.

        Raises:
            StopIteration: Raised when the maximum power of 3 is reached.
        """
        if self.power <= self.max:
            result = 3 ** self.power
            self.power += 1
            return result
        else:
            # Reset the power to 0 for the next iteration to start from the beginning.
            self.power = 0
            raise StopIteration


power = PowerOf3(6)

# The first for loop will iterate and provide the powers of 3 starting from 3^0.
for i in power:
    print(i)

# The second for loop will use the same power object, but since the power has been reset to 0,
# it will start from 3^0 again and iterate through the powers of 3.
for j in power:
    print(j)
