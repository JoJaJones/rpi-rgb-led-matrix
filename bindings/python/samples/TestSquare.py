from ArrayManipulator import ArrayManipulator
from random import randint
from constants import *

class TestSquare(ArrayManipulator):
    def __init__(self):
        self._array = []
        for r in range(NUM_ROWS):
            self._array.append([])
            for _ in range(NUM_COLS):
                self._array[r].append(randint(0, 0xFFFFFF))

    def get_canvas(self):
        return self._array

    def process_frame(self):
        greater_than_zero = False
        for row in self._array:
            for col in range(len(row)):
                row[col]//=2
                if row[col] > 0:
                    greater_than_zero = True

        return greater_than_zero
