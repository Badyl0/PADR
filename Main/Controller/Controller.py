'''
Created on Jul 5, 2019

@author: MPytel
'''
from Utils.Random import debugStatement
from Utils.Singleton import BorgSingleton
from Model.Model import Model

class Controller(BorgSingleton):
    def __init__(self):
        BorgSingleton.__init__(self)
        self._Model = Model()

    def addRecord(self, *args):
        debugStatement(2, 'User adding a new Record')
        self._Model.newRecord(args)