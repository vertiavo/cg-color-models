from tkinter import Tk, Frame, Radiobutton, Label, IntVar, Entry, Scale, HORIZONTAL

from model import Rgb, Cmyk


def clear_children(frame: Frame):
    for widget in frame.winfo_children():
        widget.destroy()


class Converter:
    DEFAULT_COLOR = 'black'

    def __init__(self, master):
        main_frame = Frame(master)
        main_frame.pack()

        # Color picker panel
        self.color_picker = Frame(main_frame)
        self.color_picker.grid(row=1, column=0)

        # Values for entry and scale in RGB
        self.rgb = Rgb(IntVar(), IntVar(), IntVar())

        # Values for entry and scale in CMYK
        self.cmyk = Cmyk(IntVar(), IntVar(), IntVar(), IntVar())

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
        radio_button_frame.grid(row=0, column=0)

    def change_panel(self):
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

    def create_cmyk_panel(self):
        clear_children(self.color_picker)

        Label(self.color_picker, text='Cyan').grid(row=0, column=0)
        Entry(self.color_picker, textvariable=self.cmyk.cyan).grid(row=0, column=1)
        Scale(self.color_picker, from_=0, to=255, orient=HORIZONTAL, variable=self.cmyk.cyan).grid(row=0, column=2)

        Label(self.color_picker, text='Magenta').grid(row=1, column=0)
        Entry(self.color_picker, textvariable=self.cmyk.magenta).grid(row=1, column=1)
        Scale(self.color_picker, from_=0, to=255, orient=HORIZONTAL, variable=self.cmyk.magenta).grid(row=1, column=2)

        Label(self.color_picker, text='Yellow').grid(row=2, column=0)
        Entry(self.color_picker, textvariable=self.cmyk.yellow).grid(row=2, column=1)
        Scale(self.color_picker, from_=0, to=255, orient=HORIZONTAL, variable=self.cmyk.yellow).grid(row=2, column=2)

        Label(self.color_picker, text='Black').grid(row=3, column=0)
        Entry(self.color_picker, textvariable=self.cmyk.black).grid(row=3, column=1)
        Scale(self.color_picker, from_=0, to=255, orient=HORIZONTAL, variable=self.cmyk.black).grid(row=3, column=2)


if __name__ == '__main__':
    root = Tk()
    app = Converter(root)
    root.mainloop()
