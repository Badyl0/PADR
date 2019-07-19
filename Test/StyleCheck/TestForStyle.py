'''
Created on 28 mar 2019

@author: Marcin
'''
import os, sys
import pycodestyle
from unittest import TestCase



class TestCodeStyle(TestCase):
    def runTest(self):
        style = pycodestyle.StyleGuide(quiet=False)
        projectDir = os.path.split(
            os.path.split(os.path.dirname(__file__))[0])[0]
        mainPath = os.path.join(projectDir, 'Main')
        pyModules = self._listPyModules(mainPath)
        result = style.check_files(pyModules)
        self.assertEqual(result.total_errors, 0, 'Found style errors!')

    def _listPyModules(self, path):
        #filesList = []
        allFileList = [(dir,file) for dir, b, file in os.walk(path)
                       if '__' not in dir]
        ## TODO: filter files for *.py
        pyList = [os.path.join(str, file) for (str, files) in allFileList
                  for file in files if ('.py' in file and '__' not in file)]
        return pyList

if __name__ == '__main__':
    TestCodeStyle().runTest()