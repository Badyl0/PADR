from Utils.tkinterImport import tkinter
from View.Layout import Layout
from Controller.Controller import Controller


class Main():
    def __init__(self):
        self._Controller = Controller()
        MainWindow = tkinter.Tk()
        layoutHandler = Layout(MainWindow)
        MainWindow.mainloop()


if __name__ == '__main__':
    Main()
