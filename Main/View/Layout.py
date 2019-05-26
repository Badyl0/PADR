'''
Created on 28 mar 2019

@author: Marcin
'''
from tkinter import *
from tkinter import ttk


class Layout():
    def __init__(self, window):
        window.title('Storage Shopping Assistant')
        mainframe = ttk.Frame(window, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)

        productName = StringVar()
        productNameEntry = ttk.Entry(mainframe, width=10,
                                     textvariable=productName)
        productNameEntry.grid(column=2, row=1, sticky=(W, E))
        ttk.Button(mainframe, text='Dodaj', command='ADD').grid(column=3,
                                                                row=1,
                                                                sticky=(W, E))
