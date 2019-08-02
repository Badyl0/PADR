'''
Created on Jul 5, 2019

@author: MPytel
'''


class BorgSingleton():
    _sharedState = {}

    def __init__(self):
        self.__dict__ = self._sharedState


if __name__ == '__main__':
    class Example(BorgSingleton):
        def __init__(self, text):
            BorgSingleton.__init__(self)
            self.text = text

        def __str__(self):
            return('Example text: %s' % self.text)


    a = Example('1')
    print(a)
    b = Example('')
    print(a,b)
    b = Example('2')
    c = Example('3')
    print(a,b,c)
    obj = object()
    print(obj)
