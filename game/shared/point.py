class Point:
    """A distance from a relative origin (0, 0)."""
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y


    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other: An instance of Point.

        Returns:
            A new instance of Point containing the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            other: An instance of Point to compare.

        Returns: 
            True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def multiply(self, factor):
        return Point(self._x * factor, self._y * factor)

    def reverse(self):
        new_x = self.x * -1
        new_y = self._y * -1
        return Point(new_x, new_y)
            