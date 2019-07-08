'''
Created on Jul 5, 2019

@author: MPytel
'''
from Utils.Singleton import BorgSingleton
from Utils.Random import debugStatement


class Model(BorgSingleton):
    def __init__(self):
        BorgSingleton.__init__(self)
        self._recordList = []

    def newRecord(self, recordParams):
        record = Record(recordParams)
        self._recordList.append(record)
        debugStatement(1, 'New record created!')


class Record():
    def _init__(self, params):
        debugStatement(2, "I'm a new record!")