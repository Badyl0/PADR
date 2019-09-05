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
        headers = self.storage.fieldnames
        records = []
        for record in self._recordList:
            records.append([])
            for field in record.__dict__.values():
                records[-1].append(field)
        #debugStatement(1, record.__dict__, 'Record')
        return (headers, records)

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
        self.dateOfPurchase = ''
        self.category = ''

    def set(self, recordParams):
        for key in recordParams:
            self.__dict__[key] = recordParams[key]
        self._calculatePricePerUnit()
        debugStatement(2, "I'm a new record! %s" % self.productName)
        return self
    
    def _calculatePricePerUnit(self):
        price = float(self.price)
        quantity = float(self.quantity)
        if self.unit == 'pcs':
            pricePerUnit = price / quantity
            sufix = ' per 1 pc'
        elif (self.unit == 'l' or self.unit == 'kg'):
            # unit = 100
            pricePerUnit = price / (quantity / 0.1)
            sufix = ' per 100 %s' % self.unit 
        elif (self.unit == 'ml' or self.unit == 'g'):
            pricePerUnit = price / (quantity / 100)
            sufix = ' per 100 %s' % self.unit
        self.pricePerSingleUnit = str(pricePerUnit) + sufix
            

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

