'''
Created on Jul 5, 2019

@author: MPytel
'''


class BorgSingleton():
    _sharedState = {}

    def __init__(self):
        self.__dict__ = self._sharedState
