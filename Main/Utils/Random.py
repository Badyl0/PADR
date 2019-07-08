'''
Created on Jul 5, 2019

@author: MPytel
'''
config_vars = {'verbo': 2}

def debugStatement(verbosity, msg):
    if(config_vars['verbo'] >= verbosity):
        print(msg)
    