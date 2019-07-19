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
        debugStatement(1, 'New record created!', __name__)

    def listRecords(self):
        records = ''
        for record in self._recordList:
            records += record.productName +'\n'
            debugStatement(1, record.value, 'Record')
        return records


class Record:
    def __init__(self, price):
        self.productName = ''
        self.quantity = {'quantity':0, 'unit':''}
        self.price = price
        self.shop = ''
        self.pricePerSingleUnit = 0
        self.dateOfBought = ''
        self.category = ''
        debugStatement(2, "I'm a new record! %s" % self.productName)
