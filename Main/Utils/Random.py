'''
Created on Jul 5, 2019

@author: MPytel
'''
config_vars = {'verbo': 2}
dev = 1


def debugStatement(verbosity, msg, prefix=''):
    if(config_vars['verbo'] >= verbosity):
        print(prefix + ': ' + msg)
