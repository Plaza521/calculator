from tkinter import *


class MainButton:
    def __init__(self, window, xpos, ypos, text, target=None):
        self.bt = Button(window, text=text, command=target)
        self.bt.place(x=xpos, y=ypos)


class Main():
    def __init__(self, label="Main window"):
        self.window = Tk()
        self.window.title(label)
        self.window.resizable(height=False, width=False)
        # self.window.geometry("54x101")

    def update(self):
        window = self.window

        output = Entry(window, width=8)
        output.place(x=0, y=0)

        MainButton(window, 00, 20, '1')
        MainButton(window, 18, 20, '2')
        MainButton(window, 36, 20, '3')
        MainButton(window, 00, 47, '4')
        MainButton(window, 18, 47, '5')
        MainButton(window, 36, 47, '6')
        MainButton(window, 00, 74, '7')
        MainButton(window, 18, 74, '8')
        MainButton(window, 36, 74, '9')

        window.mainloop()


def main():
    program = Main()
    program.update()


if __name__ == '__main__':
    main()
