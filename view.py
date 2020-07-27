#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import Entry, Label, Frame, LabelFrame, Button, Tk, Spinbox, Canvas, Scrollbar
from tkinter import ttk, IntVar
from tkinter import messagebox

# IDEAS:
# Sort Combobox of custumers with radiobuttons (by number, name1, name2)
# filter Combobox of custumers + reset filter and sort


class View(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Rechnung erstellen...")
        # -----------------------------------------------------------
        # Customer Data
        # -----------------------------------------------------------
        self.myCustomer = Customer()
        self.myCustomer.grid(row=0, column=0, sticky='nesw')

        # -----------------------------------------------------------
        # My Company Data
        # -----------------------------------------------------------
        self.myCompany = Company()
        self.myCompany.grid(row=0, column=3, sticky='nesw')

        # -----------------------------------------------------------
        # My Invoice Data
        # -----------------------------------------------------------
        self.myInvoice = Invoice()
        self.myInvoice.grid(row=3, column=0, columnspan=4, sticky='nesw')

        # -----------------------------------------------------------
        # Buttons
        # -----------------------------------------------------------
        self.btnCreate = Button(self, text="Create", width=8)
        self.btnCreate.grid(row=20, column=0)
        self.btnClose = Button(self, text="Close", width=8)
        self.btnClose.grid(row=20, column=3)

        # -----------------------------------------------------------
        # Window Size
        # -----------------------------------------------------------
        self.update()
        self.resizable(0, 0)
        self.minsize(self.winfo_width(), self.winfo_height())
        self.maxsize(self.winfo_width(), self.winfo_height())


class Customer(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(self, text="Kunde")
        start_row = 0
        # -------------------------------------------------------------------
        # Row 0 - lblframeSort
        # -------------------------------------------------------------------
        # Labels + Comboboxes
        self.lblframeSort = LabelFrame(self, text="Sortieren")
        self.lblframeSort.grid(row=start_row, column=0, sticky='w')

        self._addSortableChooseList(self.lblframeSort)

        start_row += 1

        # -------------------------------------------------------------------
        # Row 1 - lblframeData
        # -------------------------------------------------------------------
        # Customer - Labels + Entries
        self.lblframeData = LabelFrame(self, text="Kundendaten")
        self.lblframeData.grid(row=start_row, column=0, sticky='w')

        self._addDataFields(self.lblframeData)

        start_row += 1

    def _addSortableChooseList(self, master):
        # Row 0
        self.sort = IntVar()
        self.rdbName2 = ttk.Radiobutton(master, text="Nachname", variable=self.sort, value=0)
        self.rdbName2.grid(row=0, column=0, sticky='w')
        self.rdbCompany = ttk.Radiobutton(master, text="Firma", variable=self.sort, value=1)
        self.rdbCompany.grid(row=0, column=1, sticky='w')
        self.rdbNumber = ttk.Radiobutton(master, text="Kundennummer", variable=self.sort, value=2)
        self.rdbNumber.grid(row=0, column=2, sticky='w')
        # Row 1
        self.lblChoose = Label(master, text="Kunde auswählen:")
        self.lblChoose.grid(row=1, column=0, sticky='w')
        # Row 2
        self.choose = ttk.Combobox(master, width=60, state='readonly')
        self.choose.grid(row=2, column=0, sticky='w', columnspan=3, padx=1)

    def _addDataFields(self, master):
        # Row 0
        self.lblCompany = Label(master, text="Firma:")
        self.lblCompany.grid(row=0, column=0, sticky='w')
        # Row 1
        self.company = Entry(master, width=63)
        self.company.grid(row=1, column=0, columnspan=3, sticky='w', padx=1)
        # Row 2
        self.frameName = Frame(master)
        self.frameName.grid(row=2, column=0, sticky='w', columnspan=3)
        self.lblForm = Label(self.frameName, text="Anrede:")
        self.lblForm.grid(row=0, column=0, sticky='w')
        self.lblTitle = Label(self.frameName, text="Titel:")
        self.lblTitle.grid(row=0, column=1, sticky='w')
        self.form = ttk.Combobox(self.frameName, width=28)
        self.form.grid(row=1, column=0, sticky='w', padx=1)
        self.title = Entry(self.frameName, width=31)
        self.title.grid(row=1, column=1, sticky='w', padx=1)
        self.lblName1 = Label(self.frameName, text="Vorname:")
        self.lblName1.grid(row=2, column=0, sticky='w')
        self.lblName2 = Label(self.frameName, text="Nachname:")
        self.lblName2.grid(row=2, column=1, sticky='w')
        self.name1 = Entry(self.frameName, width=31)
        self.name1.grid(row=3, column=0, sticky='w', padx=1)
        self.name2 = Entry(self.frameName, width=31)
        self.name2.grid(row=3, column=1, sticky='w', padx=1)
        # Row 3
        self.lblAddress = Label(master, text="Addresse:")
        self.lblAddress.grid(row=3, column=0, sticky='w')
        # Row 4
        self.street = Entry(master, width=63)
        self.street.grid(row=4, column=0, sticky='w', columnspan=3, padx=1)
        # Row 5
        self.frameCodeCity = Frame(master)
        self.frameCodeCity.grid(row=5, column=0, sticky='w', columnspan=3)
        self.lblPostcode = Label(self.frameCodeCity, text="PLZ:")
        self.lblPostcode.grid(row=0, column=0, sticky='w')
        self.lblCity = Label(self.frameCodeCity, text="Ort:")
        self.lblCity.grid(row=0, column=1, sticky='w')
        self.postcode = Entry(self.frameCodeCity, width=10)
        self.postcode.grid(row=1, column=0, sticky='w', padx=1)
        self.city = Entry(self.frameCodeCity, width=52)
        self.city.grid(row=1, column=1, sticky='w', padx=1)
        # Row 6
        self.lblCountry = Label(master, text="Land:")
        self.lblCountry.grid(row=6, column=0, sticky='w')
        # Row 7
        self.country = Entry(master, width=63)
        self.country.grid(row=7, column=0, sticky='w', columnspan=3, padx=1)
        # Row 8
        self.btnChange = Button(master, text="Change", width=8)
        self.btnChange.grid(row=8, column=2, sticky='e')

    def editable(self, enable=True):
        state = "disabled"
        if enable:
            state = "normal"

        self.company.config(state=state)
        self.form.config(state=state)
        self.title.config(state=state)
        self.name1.config(state=state)
        self.name2.config(state=state)
        self.street.config(state=state)
        self.postcode.config(state=state)
        self.city.config(state=state)
        self.country.config(state=state)


class Company(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(self, text="Firma")
        start_row = 0
        maxColCount = 3
        # My Company - Entries
        self.lblName = Label(self, text="Meine Firma:")
        self.name = Entry(self, width=63)
        self.lblName.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.name.grid(row=start_row, column=0, columnspan=maxColCount, sticky='w', padx=1)
        start_row += 1

        self.lblAddress = Label(self, text="Addresse:")
        self.street = Entry(self, width=63)
        self.lblAddress.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.street.grid(row=start_row, column=0, columnspan=maxColCount, sticky='w', padx=1)
        start_row += 1

        self.frameCodeCity = Frame(self)
        self.lblPostcode = Label(self.frameCodeCity, text="PLZ:")
        self.postcode = Entry(self.frameCodeCity, width=10)
        self.lblCity = Label(self.frameCodeCity, text="Ort:")
        self.city = Entry(self.frameCodeCity, width=52)
        self.frameCodeCity.grid(row=start_row, column=0, sticky='w', columnspan=maxColCount)
        self.lblPostcode.grid(row=0, column=0, sticky='w')
        self.lblCity.grid(row=0, column=1, sticky='w')
        self.postcode.grid(row=1, column=0, sticky='w', padx=1)
        self.city.grid(row=1, column=1, sticky='w', padx=1)
        start_row += 1

        self.lblCountry = Label(self, text="Land:")
        self.country = Entry(self, width=63)
        self.lblCountry.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.country.grid(row=start_row, column=0, columnspan=maxColCount, sticky='w', padx=1)
        start_row += 1

        self.lblMail = Label(self, text="E-Mail:")
        self.mail = Entry(self, width=63)
        self.lblMail.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.mail.grid(row=start_row, column=0, columnspan=maxColCount, sticky='w', padx=1)
        start_row += 1

        self.lblPhone = Label(self, text="Telefon:")
        self.phone = Entry(self, width=63)
        self.lblPhone.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.phone.grid(row=start_row, column=0, columnspan=maxColCount, sticky='w', padx=1)
        start_row += 1

        self.lblBank = Label(self, text="Bank:")
        self.bank = Entry(self, width=63)
        self.lblIban = Label(self, text="IBAN:")
        self.iban = Entry(self, width=63)
        self.lblBic = Label(self, text="BIC:")
        self.bic = Entry(self, width=63)
        self.lblBank.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.bank.grid(row=start_row, column=0, columnspan=maxColCount, sticky='w', padx=1)
        start_row += 1
        self.lblIban.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.iban.grid(row=start_row, column=0, columnspan=maxColCount, sticky='w', padx=1)
        start_row += 1
        self.lblBic.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.bic.grid(row=start_row, column=0, columnspan=maxColCount, sticky='w', padx=1)
        start_row += 1


class Invoice(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(self, text="Rechnungsdaten")
        self.partList = []

        self.row = 0

        self.lblNumber = Label(self, text="Rechnungsnummer:")
        self.number = Spinbox(self, from_=1, to=1000000, wrap=True, increment=1)
        self.btnAdd = Button(self, text="+", width=2)

        self.lblNumber.grid(row=self.row, column=0, sticky='w')
        self.row += 1
        self.number.grid(row=self.row, column=0, sticky='w')
        self.btnAdd.grid(row=self.row, column=9, sticky='e')
        self.row += 1

        # Data Frame with scrollable Data Fields
        self.frameData = Frame(self)
        self.frameData.grid(row=self.row, column=0, columnspan=10)
        self.canvas = Canvas(self.frameData, width=875)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        self.canvasFrame = Frame(self.canvas)
        self.canvas.create_window(0, 0, window=self.canvasFrame, anchor='nw')

        self.myScrollbar = Scrollbar(self.frameData, orient='vertical')
        self.myScrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.myScrollbar.set)
        self.myScrollbar.grid(row=0, column=1, sticky="nse")

        self.canvasFrame.bind("<Configure>", lambda e: self.scrollregion())

        self.row = 0

        self.lblQuantity = Label(self.canvasFrame, text="Menge:")
        self.lblUnit = Label(self.canvasFrame, text="Einheit:")
        self.lblDescription = Label(self.canvasFrame, text="Beschreibung:")
        self.lblPricePerUnit = Label(self.canvasFrame, text="Stückpreis:")

        self.lblQuantity.grid(row=self.row, column=0, sticky='w')
        self.lblUnit.grid(row=self.row, column=1, sticky='w')
        self.lblDescription.grid(row=self.row, column=2, columnspan=2, sticky='w')
        self.lblPricePerUnit.grid(row=self.row, column=4, sticky='w')
        self.row += 1

        self.addPart()

    def scrollregion(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.yview_moveto(1)

    def addPart(self):
        self.partList.append(self.Part(self))

    class Part():
        def __init__(self, root):
            self.root = root
            self.quantity = None
            self.unit = None
            self.description = None
            self.pricePerUnit = None

            self.addLine()

        def addLine(self):
            print("Add line")
            self.quantity = Entry(self.root.canvasFrame)
            self.unit = Entry(self.root.canvasFrame, width=30)
            self.description = Entry(self.root.canvasFrame, width=60)
            self.pricePerUnit = Entry(self.root.canvasFrame, width=30)

            self.quantity.grid(row=self.root.row, column=0, sticky='w')
            self.unit.grid(row=self.root.row, column=1, sticky='w')
            self.description.grid(row=self.root.row, column=2, columnspan=2, sticky='w')
            self.pricePerUnit.grid(row=self.root.row, column=4, sticky='w')
            self.root.row += 1

        def clear(self):
            self.quantity.delete(0, 'end')
            self.unit.delete(0, 'end')
            self.description.delete(0, 'end')
            self.pricePerUnit.delete(0, 'end')
            self.unit.delete(0, 'end')
