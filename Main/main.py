from Utils.tkinterImport import tkinter
from View.Layout import Layout


class Main():
    def __init__(self):
        MainWindow = tkinter.Tk()
        layoutHandler = Layout(MainWindow)
        MainWindow.mainloop()


if __name__ == '__main__':
    Main()
