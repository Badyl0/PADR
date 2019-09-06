'''
Created on Jul 5, 2019

@author: MPytel
'''
from Utils.Random import debugStatement
from Utils.Singleton import BorgSingleton


class Controller(BorgSingleton):
    def __init__(self):
        BorgSingleton.__init__(self)

    def addView(self, viewObject):
        self._View = viewObject

    def addModel(self, modelObject):
        self._Model = modelObject

    def startApp(self):
        self._View.start()

    def addRecord(self, value):
        debugStatement(2, 'User adding a new Record')
        self._Model.newRecord(value)

    def listRecords(self):
        return self._Model.listRecords()

    def exit(self):
        self._Model.saveRecords()
        self._View.mainView.MainWindow.destroy()
