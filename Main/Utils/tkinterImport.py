'''
Created on Jul 5, 2019

@author: MPytel
'''
from sys import version_info as python


if python.major is 3:
    import tkinter as tkinter
    import tkinter.ttk as ttk
    import tkinter.constants as constants
elif python.major is 2:
    raise Exception("Python interpreter version 2!")
    import Tkinter as tkinter
