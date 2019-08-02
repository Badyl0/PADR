'''
Created on Jul 5, 2019

@author: MPytel
'''
from Utils.Singleton import BorgSingleton
from Utils.Random import debugStatement
from csv import DictWriter, DictReader


class Model(BorgSingleton):
    def __init__(self):
        BorgSingleton.__init__(self)
        self.storage = Storage()
        self._recordList = self.storage.loadStoredRecords()
        self.storage.open()

    def newRecord(self, recordParams):
        record = Record().set(recordParams)
        self._recordList.append(record)
        self._updateStorage(record)
        debugStatement(1, 'New record created!', __name__)

    def listRecords(self):
        records = ''
        for record in self._recordList:
            records += record.productName + ('\t%s' % record.price) +'\n'
            
            debugStatement(1, record.price, 'Record')
        return records

    def _createStorage(self, name):
        return open(name, 'w')

    def _updateStorage(self, recordIns):
        self.storage.writeln(recordIns.__dict__)

    def saveRecords(self):
        self.storage.close()

class Record:
    def __init__(self):
        self.productName = ''
        self.quantity = 0
        self.unit = ''
        self.price = 0
        self.shop = ''
        self.pricePerSingleUnit = 0
        self.dateOfBought = ''
        self.category = ''

    def set(self, recordParams):
        self.price = recordParams['price']
        debugStatement(2, "I'm a new record! %s" % self.productName)
        return self

class Storage(BorgSingleton):
    def __init__(self):
        BorgSingleton.__init__(self)
        self.fieldnames = list(Record().__dict__.keys())

    def open(self):
        self.file = open('StorageFile.csv', 'a')
        self.csvWriter = DictWriter(self.file, self.fieldnames)

    def loadStoredRecords(self):
        with open('StorageFile.csv', 'r') as storageFile:
            csvReader = DictReader(storageFile, self.fieldnames)
            storedRecords = [Record().set(row) for row in csvReader]
        return storedRecords

    def close(self):
        self.file.close()

    def writeln(self, recordDict):
        self.csvWriter.writerow(recordDict)

