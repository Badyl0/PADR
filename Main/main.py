from tkinter import Tk
from View.Layout import Layout

class Main():
    def __init__(self):        
        MainWindow = Tk()
        layoutHandler = Layout(MainWindow)
        MainWindow.mainloop()
        

if __name__ == '__main__':
    Main()


