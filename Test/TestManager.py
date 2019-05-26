'''
Created on 12 kwi 2019

@author: Marcin
'''
import sys
import unittest
from StyleCheck.TestForStyle import TestCodeStyle

ROOT_DIR = ('D:\eclipse-workspace\SSA')

def main():
    testSuite = unittest.TestSuite()
    testSuite.addTest(TestCodeStyle('testStyle'))
    testRunner = unittest.TextTestRunner()
    testRunner.run(testSuite)
    

if __name__ == '__main__':
    main()