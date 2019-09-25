'''
Created on Jul 5, 2019

@author: MPytel
'''
from Utils.Singleton import BorgSingleton
from Utils.Random import debugStatement, truncate
from csv import DictWriter, DictReader


class Model(BorgSingleton):
    def __init__(self):
        BorgSingleton.__init__(self)
        self._nextRecordID = 0
        self.storage = Storage()
        self._recordList = self.storage.loadStoredRecords()
        self._setNextRecordID()
        self.storage.open()

    def newRecord(self, recordParams):
        recordParams.update({'id': self._nextRecordID})
        record = Record().set(recordParams)
        self._recordList.append(record)
        self._updateStorage(record)
        debugStatement(1, 'New record created!', __name__)

    def getRecordFields(self, id=None):
        if id is not None:
            for record in self._recordList:
                if record.id == id:
                    return record.__dict__
            raise KeyError("Record %s doesn't exist!" % id)

    def getRecord(self, id=None):
        if id is not None:
            for record in self._recordList:
                if record.id == id:
                    return record
            raise KeyError("Record %s doesn't exist!" % id)

    def updateRecord(self, fields):
        record = self.getRecord(fields['id'])
        del fields['id']
        record.set(fields)

    def listRecords(self):
        headers = self.storage.fieldnames
        records = []
        for record in self._recordList:
            #records.append([])
            records.append(self.getSingleRecordFields(record))
        return (headers, records)

    def getSingleRecordFields(self, record):
        fieldList = []
        for field in record.__dict__.values():
                fieldList.append(field)
        return fieldList

    def _createStorage(self, name):
        return open(name, 'w')

    def _updateStorage(self, recordIns):
        self.storage.writeln(recordIns.__dict__)

    def saveRecords(self):
        self.storage.close()

    def _setNextRecordID(self):
        recordsIDs = [int(record.id) for record in self._recordList]
        if any(recordsIDs):
            self._nextRecordID = max(recordsIDs) + 1


class Record:
    def __init__(self):
        self.id = 0
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
            pricePerUnit = truncate(price / quantity, 100)
            sufix = ' per 1 pc'
        elif (self.unit == 'l' or self.unit == 'kg'):
            # unit = 100
            pricePerUnit = truncate(price / (quantity / 0.1), 100)
            if self.unit == 'l':
                unit = 'ml'
            elif self.unit == 'kg':
                unit = 'g'
            sufix = ' per 100 %s' % unit
        elif (self.unit == 'ml' or self.unit == 'g'):
            pricePerUnit = truncate(price / (quantity / 100), 100)
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
