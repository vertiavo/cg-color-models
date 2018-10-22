from tkinter import ALL, Canvas, Entry, Frame, HORIZONTAL, IntVar, Label, Radiobutton, Scale, Tk

from model import Cmyk, Rgb


def clear_children(frame: Frame):
    for widget in frame.winfo_children():
        widget.destroy()


class Converter:
    DEFAULT_COLOR = 'black'
    SQUARE_COORDS = (0, 0, 300, 300)

    def __init__(self, master):
        main_frame = Frame(master)
        main_frame.pack()

        # Color picker panel
        self.color_picker = Frame(main_frame)
        self.color_picker.grid(row=1, column=0)

        # Converted color panel
        self.converted_color = Frame(main_frame)
        self.converted_color.grid(row=1, column=2)

        # Values for entry and scale in RGB
        self.rgb = self.initialize_rgb()

        # Values for entry and scale in CMYK
        self.cmyk = self.initialize_cmyk()
        # Color preview panel
        self.canvas = Canvas(main_frame, width=300, height=300)
        self.canvas.create_rectangle(0, 0, 300, 300, fill=self.DEFAULT_COLOR)
        self.canvas.grid(row=1, column=1)

        # Color model selector section
        self.selected_model = IntVar()
        self.selected_model.set(1)

        radio_button_frame = Frame(main_frame)
        Label(radio_button_frame, text='Choose color model').grid(row=0, columnspan=2)

        rgb_button = Radiobutton(radio_button_frame, text='RGB', variable=self.selected_model, value=1,
                                 command=self.change_panel)
        rgb_button.grid(row=1, column=0)
        rgb_button.invoke()

        Radiobutton(radio_button_frame, text='CMYK', variable=self.selected_model, value=2,
                    command=self.change_panel).grid(row=1, column=1)
        radio_button_frame.grid(row=0, columnspan=2)

    def initialize_rgb(self):
        rgb = Rgb()
        rgb.red.trace_add("write", self.callback)
        rgb.green.trace_add("write", self.callback)
        rgb.blue.trace_add("write", self.callback)

        return rgb

    def initialize_cmyk(self):
        cmyk = Cmyk()
        cmyk.cyan.trace_add("write", self.callback)
        cmyk.magenta.trace_add("write", self.callback)
        cmyk.yellow.trace_add("write", self.callback)
        cmyk.black.trace_add("write", self.callback)

        return cmyk

    def callback(self, param1, param2, param3):
        if self.selected_model.get() is 1:
            self.calculate_cmyk()
        else:
            self.calculate_rgb()
        color = '#%02x%02x%02x' % (self.rgb.red.get(), self.rgb.green.get(), self.rgb.blue.get())
        self.redraw_rectangle(color)

    def calculate_cmyk(self):
        red_ = self.rgb.red.get() / 255
        green_ = self.rgb.green.get() / 255
        blue_ = self.rgb.blue.get() / 255

        black_value = 1 - max(red_, green_, blue_)
        if black_value == 1:
            cyan_value = 0.0
            magenta_value = 0.0
            yellow_value = 0.0
        else:
            cyan_value = (1 - red_ - black_value) / (1 - black_value)
            magenta_value = (1 - green_ - black_value) / (1 - black_value)
            yellow_value = (1 - blue_ - black_value) / (1 - black_value)

        self.cmyk.black.set(black_value)
        self.cmyk.cyan.set(cyan_value)
        self.cmyk.magenta.set(magenta_value)
        self.cmyk.yellow.set(yellow_value)

        # self.cmyk.black.set(min(1 - self.rgb.red.get(), 1 - self.rgb.green.get(), 1 - self.rgb.blue.get()))
        # self.cmyk.cyan.set((1 - self.rgb.red.get() - self.cmyk.black.get()) / (1 - self.cmyk.black.get()))
        # self.cmyk.magenta.set((1 - self.rgb.green.get() - self.cmyk.black.get()) / (1 - self.cmyk.black.get()))
        # self.cmyk.yellow.set((1 - self.rgb.blue.get() - self.cmyk.black.get()) / (1 - self.cmyk.black.get()))

    def calculate_rgb(self):
        cyan_ = self.cmyk.cyan.get() / 100
        magenta_ = self.cmyk.magenta.get() / 100
        yellow_ = self.cmyk.yellow.get() / 100
        black_ = self.cmyk.black.get() / 100

        self.rgb.red.set(255 * (1 - cyan_) * (1 - black_))
        self.rgb.green.set(255 * (1 - magenta_) * (1 - black_))
        self.rgb.blue.set(255 * (1 - yellow_) * (1 - black_))

        # self.rgb.red.set(1 - min(1, cyan_ * (1 - black_) + black_))
        # self.rgb.green.set(1 - min(1, magenta_ * (1 - black_) + black_))
        # self.rgb.blue.set(1 - min(1, yellow_ * (1 - black_) + black_))

    def redraw_rectangle(self, color):
        self.canvas.delete(ALL)

        self.canvas.create_rectangle(*self.SQUARE_COORDS, fill=color)

    def change_panel(self):
        self.rgb = self.initialize_rgb()
        self.cmyk = self.initialize_cmyk()
        self.redraw_rectangle(self.DEFAULT_COLOR)
        if self.selected_model.get() is 1:
            print('RGB selected')
            self.create_rgb_panel()
        else:
            print('CMYK selected')
            self.create_cmyk_panel()

    def create_rgb_panel(self):
        clear_children(self.color_picker)

        Label(self.color_picker, text='Red').grid(row=0, column=0)
        Entry(self.color_picker, textvariable=self.rgb.red).grid(row=0, column=1)
        Scale(self.color_picker, from_=0, to=255, orient=HORIZONTAL, variable=self.rgb.red).grid(row=0, column=2)

        Label(self.color_picker, text='Green').grid(row=1, column=0)
        Entry(self.color_picker, textvariable=self.rgb.green).grid(row=1, column=1)
        Scale(self.color_picker, from_=0, to=255, orient=HORIZONTAL, variable=self.rgb.green).grid(row=1, column=2)

        Label(self.color_picker, text='Blue').grid(row=2, column=0)
        Entry(self.color_picker, textvariable=self.rgb.blue).grid(row=2, column=1)
        Scale(self.color_picker, from_=0, to=255, orient=HORIZONTAL, variable=self.rgb.blue).grid(row=2, column=2)

        clear_children(self.converted_color)

        Label(self.converted_color, text='Cyan').grid(row=0, column=0)
        Entry(self.converted_color, textvariable=self.cmyk.cyan).grid(row=0, column=1)

        Label(self.converted_color, text='Magenta').grid(row=1, column=0)
        Entry(self.converted_color, textvariable=self.cmyk.magenta).grid(row=1, column=1)

        Label(self.converted_color, text='Yellow').grid(row=2, column=0)
        Entry(self.converted_color, textvariable=self.cmyk.yellow).grid(row=2, column=1)

        Label(self.converted_color, text='Black').grid(row=3, column=0)
        Entry(self.converted_color, textvariable=self.cmyk.black).grid(row=3, column=1)

    def create_cmyk_panel(self):
        clear_children(self.color_picker)

        Label(self.color_picker, text='Cyan').grid(row=0, column=0)
        Entry(self.color_picker, textvariable=self.cmyk.cyan).grid(row=0, column=1)
        Scale(self.color_picker, from_=0, to=100, orient=HORIZONTAL, variable=self.cmyk.cyan).grid(row=0, column=2)

        Label(self.color_picker, text='Magenta').grid(row=1, column=0)
        Entry(self.color_picker, textvariable=self.cmyk.magenta).grid(row=1, column=1)
        Scale(self.color_picker, from_=0, to=100, orient=HORIZONTAL, variable=self.cmyk.magenta).grid(row=1, column=2)

        Label(self.color_picker, text='Yellow').grid(row=2, column=0)
        Entry(self.color_picker, textvariable=self.cmyk.yellow).grid(row=2, column=1)
        Scale(self.color_picker, from_=0, to=100, orient=HORIZONTAL, variable=self.cmyk.yellow).grid(row=2, column=2)

        Label(self.color_picker, text='Black').grid(row=3, column=0)
        Entry(self.color_picker, textvariable=self.cmyk.black).grid(row=3, column=1)
        Scale(self.color_picker, from_=0, to=100, orient=HORIZONTAL, variable=self.cmyk.black).grid(row=3, column=2)

        clear_children(self.converted_color)

        Label(self.converted_color, text='Red').grid(row=0, column=0)
        Entry(self.converted_color, textvariable=self.rgb.red).grid(row=0, column=1)

        Label(self.converted_color, text='Green').grid(row=1, column=0)
        Entry(self.converted_color, textvariable=self.rgb.green).grid(row=1, column=1)

        Label(self.converted_color, text='Blue').grid(row=2, column=0)
        Entry(self.converted_color, textvariable=self.rgb.blue).grid(row=2, column=1)


if __name__ == '__main__':
    root = Tk()
    app = Converter(root)
    root.mainloop()
