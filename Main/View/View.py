'''
Created on Jul 12, 2019

@author: MPytel
'''
from Utils.Singleton import BorgSingleton
from View.Layout import Layout
from Utils.Random import debugStatement


class View(BorgSingleton):
    def __init__(self):
        BorgSingleton.__init__(self)

    def initMainView(self):
        self.mainView = Layout()

    def addController(self, controller):
        self._Controller = controller

    def start(self):
        self.mainView.startMainLoop()

    def addRecord(self, value):
        debugStatement(2, 'addRecord %s' % value)
        self._Controller.addRecord(value)

    def listRecords(self):
        return self._Controller.listRecords()
