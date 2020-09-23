from DisplayBase import DisplayBase
from TestSquare import TestSquare

class ArrayDisplay(DisplayBase):
    def __init__(self, *args, **kwargs):
        super(ArrayDisplay, self).__init__(*args, **kwargs)
        self._array_manipulator = None
        self._array = None

    def add_array_manipulator(self, array_manipulator):
        self._array_manipulator = array_manipulator
        self._array = self._array_manipulator.get_canvas()

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        height = len(self._array)
        width = len(self._array[0])
        while True:
            for x in range(width):
                for y in (height):
                    color = self._array[y][x]
                    r = (color &0xFF0000) >> 16
                    g = (color & 0xFF00) >> 8
                    b = (color & 0xFF)
                    offset_canvas.SetPixel(x, y, r, g, b)

            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
            self.usleep(100*1000)
            if not self._array_manipulator.process_frame():
                break


if __name__ == "__main__":
    array_display = ArrayDisplay()
    array_display.add_array_manipulator(TestSquare())
    if (not array_display.process()):
        array_display.print_help()