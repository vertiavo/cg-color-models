from tkinter import IntVar


class Rgb(object):

    def __init__(self):
        self._red = IntVar()
        self._green = IntVar()
        self._blue = IntVar()

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        self._red = value

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, value):
        self._green = value

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, value):
        self._blue = value


class Cmyk(object):

    def __init__(self):
        self._cyan = IntVar()
        self._magenta = IntVar()
        self._yellow = IntVar()
        self._black = IntVar()

    @property
    def cyan(self):
        return self._cyan

    @cyan.setter
    def cyan(self, value):
        self._cyan = value

    @property
    def magenta(self):
        return self._magenta

    @magenta.setter
    def magenta(self, value):
        self._magenta = value

    @property
    def yellow(self):
        return self._yellow

    @yellow.setter
    def yellow(self, value):
        self._yellow = value

    @property
    def black(self):
        return self._black

    @black.setter
    def black(self, value):
        self._black = value
