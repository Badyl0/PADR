'''
Created on Jul 5, 2019

@author: MPytel
'''
config_vars = {'verbo': 2}
dev = 1

unitsList = ['ml', 'kg', 'pcs', 'l', 'g']


def debugStatement(verbosity, msg, prefix=''):
    if(config_vars['verbo'] >= verbosity):
        print(prefix + ': ' + msg)
