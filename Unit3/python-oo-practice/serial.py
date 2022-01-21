"""Python serial number generator."""

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
    
    """
    Constructor for SerialGenerator that assigns the start value
    passed through to a class attribute.
    """
    def __init__(self, start=100):
        self.start = start
    

    """
    Generate method that increments start number
    """
    def generate(self):
        print(self.start)
        self.start += 1 

    """
    Reset method that resets the number back to 100
    """
    def reset(self):
        self.start = 100

    def __repr__(self):
        return "SerialGenerator(start={current} next={next})".format(current=self.start, next=self.start + 1)
