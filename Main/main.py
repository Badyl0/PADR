from Utils.tkinterImport import tkinter
from Controller.Controller import Controller
from Model.Model import Model
from View.View import View


class Main():
    def __init__(self):
        self._Controller = Controller()
        self._View = View()
        self._Model = Model()

        self._Controller.addView(self._View)
        self._Controller.addModel(self._Model)
        self._View.addController(self._Controller)

        self._View.initMainView()

        self._Controller.startApp()


if __name__ == '__main__':
    Main()
