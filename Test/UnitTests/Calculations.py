from unittest import TestCase
from Model.Model import Record 

class TestPricePerSingleUnit(TestCase):
    def testPricePerUnit(self):
        priceUnitList = [(10, 1, 'l'),
                         (5, 1, 'kg'),
                         (200, 100, 'g'),
                         (9.5, 60, 'ml')]
        expectedResult = ['1.0 per 100 ml',
                          '0.5 per 100 g',
                          '200.0 per 100 g',
                          '15.83 per 100 ml']
        testRecord = Record()
        resultArray = []
        for price, quantity, unit in priceUnitList:
            testRecord.price = price
            testRecord.unit = unit
            testRecord.quantity = quantity
            testRecord._calculatePricePerUnit()
            resultArray.append(testRecord.pricePerSingleUnit)
        self.assertListEqual(expectedResult, resultArray)