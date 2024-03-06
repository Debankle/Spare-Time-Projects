"""Simple implementation of a spiral printing function"""

import random
from enum import Enum
import math

# TODO: Replace direction with quaternions and have a rotation 
#       calculation vector to one line the calculateDirection
# This should also allow for clockwise/anticlockwise with a multiplier somehow


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


class SpiralPrint():
    """
    SpiralPrint Class definition

    This class takes in a number, and generates a spiral structure
    that can be printed to the console to that number

    This class should only be accessed with the print function
    using the overriden __str__ method, in order to print the spiral
    """

    def __init__(self, max_num: int, start_num: int = 1):
        """
        Initialize a new instance of SpiralPrint

        Args:
            max_num: The maximum number the spiral goes to
            start_num: The initial central number of the spiral. Defaults to 1
        """
        self._max_num = max_num
        self._start_num = start_num
        self._dir = Direction.RIGHT

        self._calculate()

    def _calculate(self):
        """
        Calculate the values in each position of the spiral array
        as the spiral goes around. Iterates from the start number to
        the max number in a clockwise spiral
        """

        self._num_nums = self._max_num + 1 - self._start_num
        self._size = math.ceil(math.sqrt(self._num_nums))
        self._center = math.ceil(self._size / 2) - 1
        self._x = self._y = self._center
        self._max_size = len(str(self._max_num))

        self._spiral_nums = [[None for _ in range(0, self._size)] for _ in range(0, self._size)]

        self._i = self._start_num
        self._spiral_nums[self._x][self._y] = self._i

        while self._i < self._max_num:
            self._i += 1
            self._move_current_point()
            self._spiral_nums[self._x][self._y] = self._i

    def _move_current_point(self):
        """
        Using the current x and y points, and the direction being pointed
        move the current position in the spiral array by 1 in the direction
        and calculate where to move to next
        """
        if self._dir == Direction.RIGHT:
            self._y += 1
            if self._spiral_nums[self._x + 1][self._y] is None:
                self._dir = Direction.DOWN
        elif self._dir == Direction.LEFT:
            self._y -= 1
            if self._spiral_nums[self._x - 1][self._y] is None:
                self._dir = Direction.UP
        elif self._dir == Direction.UP:
            self._x -= 1
            if self._spiral_nums[self._x][self._y + 1] is None:
                self._dir = Direction.RIGHT
        elif self._dir == Direction.DOWN:
            self._x += 1
            if self._spiral_nums[self._x][self._y - 1] is None:
                self._dir = Direction.LEFT
        else:
            raise AssertionError("How did I get here?")

    def __str__(self):
        """
        An override of __str__ to ensure that the print correctly
        prints a spiral of the calculated spiral numbers in the
        stored array
        """
        spiral = ''
        for line in self._spiral_nums:
            for item in line:
                if item is None:
                    spiral += ' ' * (self._max_size + 1)
                else:
                    spiral += ' ' * (self._max_size - len(str(item))) + str(item) + ' '
            spiral += '\n'
        return spiral


if __name__ == "__main__":
    for _ in range(5):
        num = random.randint(1,200)
        print(SpiralPrint(num))
        print()

    for _ in range(5):
        num = random.randint(50,200)
        print(SpiralPrint(num, start_num=math.floor(num/2)))
        print()
