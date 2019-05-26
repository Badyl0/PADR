'''
Created on 28 mar 2019

@author: Marcin
'''
import os, sys
import pycodestyle
from unittest import TestCase



class TestCodeStyle(TestCase):
    def testStyle(self):
        style = pycodestyle.StyleGuide(quiet=False)
        file = os.path.join('D:/eclipse-workspace', 'SSA', 'Main',
                            'View', 'Layout.py')
        result = style.check_files([file,])
        self.assertEqual(result.total_errors, 0, 'Found style errors!')
        
        
if __name__ == '__main__':
    TestCodeStyle()