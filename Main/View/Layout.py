'''
Created on 28 mar 2019

@author: Marcin
'''
from Utils.tkinterImport import tkinter, ttk, constants
from Utils.Random import debugStatement, dev, unitsList



class Layout():
    def __init__(self, ):
        self.MainWindow = tkinter.Tk()
        self.MainWindow.title('Storage Shopping Assistant')
        mainframe = ttk.Frame(self.MainWindow, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(tkinter.N,
                                                tkinter.W,
                                                tkinter.E,
                                                tkinter.S))
        self.MainWindow.columnconfigure(0, weight=1)
        self.MainWindow.rowconfigure(0, weight=1)
        self._RecordField = NewRecordField(mainframe,
                                           self.newRecordAction)
        if dev:
            self._listingRecordsField = ListingRecordsField(
                mainframe,
                self.displayRecords)
        self._onExitAction()

    def startMainLoop(self):
        self.MainWindow.mainloop()

    def _onExitAction(self):
        from Controller.Controller import Controller
        self.MainWindow.protocol("WM_DELETE_WINDOW", Controller().exit)

    def newRecordAction(self):
        from View.View import View
        debugStatement(2, 'adding record')

        view = View()
        recordFields = dict([(var._name, var.get()) for var 
                             in self._RecordField.__dict__.values()])
        view.addRecord(recordFields)
        self._RecordField.clear()
        self._RecordField.productName.set("")

    def displayRecords(self):
        from View.View import View
        view = View()
        headers, records = view.listRecords()
        columns = records.insert(0, headers)
        columns = [*zip(*records)]
        '''
        TBD: check len of column, pretty print list
        '''
        pass

class BasicField():
    def __init__(self, frame):
        pass


class NewRecordField(BasicField):
    def __init__(self, frame, action):
        self.productName = tkinter.StringVar(name='productName')
        self.price = tkinter.StringVar(name='price')
        self.unit = tkinter.StringVar(name='unit')
        self.quantity = tkinter.StringVar(name='quantity')

        ttk.Label(frame, text='ProductName').grid(
            column=1, row=1, sticky=(tkinter.W, tkinter.E))
        ttk.Entry(frame, width=20, textvariable=self.productName).grid(
            column=1, row=2, sticky=(tkinter.W, tkinter.E))

        ttk.Label(frame, text='Price').grid(
            column=2, row=1, sticky=(tkinter.W, tkinter.E))
        ttk.Entry(frame, width=20, textvariable=self.price).grid(
            column=2, row=2, sticky=(tkinter.W, tkinter.E))

        ttk.Label(frame, text='Unit').grid(
            column=3, row=1, sticky=(tkinter.W, tkinter.E))
        ttk.Combobox(frame, width=20, textvariable=self.unit,
                     values=unitsList).grid(
            column=3, row=2, sticky=(tkinter.W, tkinter.E))

        ttk.Label(frame, text='Quantity').grid(
            column=4, row=1, sticky=(tkinter.W, tkinter.E))
        ttk.Entry(frame, width=10, textvariable=self.quantity).grid(
            column=4, row=2, sticky=(tkinter.W, tkinter.E))

        ttk.Button(frame, text='AddRecord', command=action).grid(
                   column=5, row=2, sticky=(tkinter.N, tkinter.E))

    def clear(self):
        for Var in self.__dict__.items():
            Var[1].set("")


class ListingRecordsField(BasicField):
    def __init__(self, frame, action):
        self.recordList = tkinter.StringVar()
        self.recordDisplay = tkinter.Text(frame, width=100, height=10)
        self.recordDisplay.grid(column=0,row=5, columnspan=4)
        ttk.Button(frame, text='ShowRecords', command=action). grid(row=5,
                                                                   column=3)
        