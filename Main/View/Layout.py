'''
Created on 28 mar 2019

@author: Marcin
'''
from Utils.tkinterImport import tkinter, ttk
from Utils.Random import debugStatement, dev


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

    def startMainLoop(self):
        self.MainWindow.mainloop()

    def newRecordAction(self):
        from View.View import View
        debugStatement(2, 'adding record')

        view = View()
        view.addRecord(self._RecordField.productName.get())

    def displayRecords(self):
        from View.View import View
        view = View()
        self._listingRecordsField.recordList.set(view.listRecords())

class BasicField():
    def __init__(self, frame):
        pass


class NewRecordField(BasicField):
    def __init__(self, frame, action):
        self.productName = tkinter.StringVar()
        productNameEntry = ttk.Entry(frame, width=10,
                                     textvariable=self.productName)
        productNameEntry.grid(column=2, row=1, sticky=(tkinter.W, tkinter.E))
        ttk.Button(frame, text='Dodaj',
                   command=action).grid(
                       column=3, row=1, sticky=(tkinter.W, tkinter.E))


class ListingRecordsField(BasicField):
    def __init__(self, frame, action):
        self.recordList = tkinter.StringVar()
        recordDisplay = ttk.Entry(frame, width=100, height=50,
                                     textvariable=self.recordList)
        recordDisplay.grid(row=4)
        ttk.Button(frame, text='PokazWpisy', command=action). grid(row=2,
                                                                   column=3)
        