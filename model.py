class Rgb(object):

    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

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

    def __init__(self, cyan, magenta, yellow, black):
        self._cyan = cyan
        self._magenta = magenta
        self._yellow = yellow
        self._black = black

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
