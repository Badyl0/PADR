'''
Created on 12 kwi 2019

@author: Marcin
'''
import sys
import unittest
from StyleCheck.TestForStyle import TestCodeStyle
from UnitTests.Calculations import TestPricePerSingleUnit

def main():
    testSuite = unittest.TestSuite()
    testSuite.addTest(TestCodeStyle())
    testSuite.addTest(TestPricePerSingleUnit('testPricePerUnit'))
    testRunner = unittest.TextTestRunner()
    testRunner.run(testSuite)

if __name__ == '__main__':
    main()