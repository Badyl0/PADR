'''
Created on 28 mar 2019

@author: Marcin
'''
from Utils.tkinterImport import tkinter, ttk
from Controller.Controller import Controller


class Layout():
    def __init__(self, window):
        self._Controller = Controller()
        window.title('Storage Shopping Assistant')
        mainframe = ttk.Frame(window, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(tkinter.N,
                                                tkinter.W,
                                                tkinter.E,
                                                tkinter.S))
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)

        productName = tkinter.StringVar()
        productNameEntry = ttk.Entry(mainframe, width=10,
                                     textvariable=productName)
        productNameEntry.grid(column=2, row=1, sticky=(tkinter.W, tkinter.E))
        ttk.Button(mainframe, text='Dodaj', command=self._Controller.addRecord)\
        .grid(column=3, row=1, sticky=(tkinter.W, tkinter.E))
