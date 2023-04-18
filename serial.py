class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create serial generator from start value with a property to hold the increment"""
        self.start = self.current_increment = start

    def generate(self):
        """Return the next number in the sequence and update the increment"""
        self.current_increment += 1
        return self.current_increment -1

    def reset(self):
        """Reset increment to start"""
        self.current_increment = self.start
