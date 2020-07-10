#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import Entry, Label, Frame, LabelFrame, Button, Tk, Spinbox, Canvas, Scrollbar
from tkinter import ttk
from tkinter import messagebox

# IDEAS:
# Sort Combobox of custumers with radiobuttons (by number, name1, name2)
# filter Combobox of custumers + reset filter and sort
# Mindestgröße / Maximalgröße

class View(Tk):
    def __init__(self):
        Tk.__init__(self)
        #-----------------------------------------------------------
        # Customer Data
        #-----------------------------------------------------------
        self.myCustomer = Customer()
        self.myCustomer.grid(row=0, column=0, sticky='nesw')

        #-----------------------------------------------------------
        # My Company Data
        #-----------------------------------------------------------
        self.myCompany = Company()
        self.myCompany.grid(row=0, column=3, sticky='nesw')

        #-----------------------------------------------------------
        # My Invoice Data
        #-----------------------------------------------------------
        self.myInvoice = Invoice()
        self.myInvoice.grid(row=3, column=0, columnspan=4, sticky='nesw')

        #-----------------------------------------------------------
        # Buttons
        #-----------------------------------------------------------
        self.btnCreate = Button(self, text="Create", width=8)
        self.btnCreate.grid(row=20, column=0)
        self.btnClose = Button(self, text="Close", width=8)
        self.btnClose.grid(row=20, column=3)


class Customer(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(self, text="Kunde")
        start_row = 0
        maxColCount = 3
        # Customer - Labels + Comboboxes 
        self.lblChoose = Label(self, text="Kunde auswählen:")
        self.choose = ttk.Combobox(self, width=60, state='readonly')
        self.lblChoose.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.choose.grid(row=start_row, column=0, sticky='w', columnspan=maxColCount, padx=1)
        start_row += 1

        # Customer - Labels + Entries
        self.lblCompany = Label(self, text="Firma:")
        self.company = Entry(self, width=63)
        self.frameName = Frame(self)
        self.lblName1 = Label(self.frameName, text="Vorname:")
        self.lblName2 = Label(self.frameName, text="Nachname:")
        self.name1 = Entry(self.frameName, width=31)
        self.name2 = Entry(self.frameName, width=31)
        self.lblCompany.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.company.grid(row=start_row, column=0, columnspan=maxColCount, sticky='w', padx=1)
        start_row += 1
        self.frameName.grid(row=start_row, column=0, sticky='w', columnspan=maxColCount)
        self.lblName1.grid(row=0, column=0, sticky='w')
        self.lblName2.grid(row=0, column=1, sticky='w')
        self.name1.grid(row=1, column=0, sticky='w', padx=1)
        self.name2.grid(row=1, column=1, sticky='w', padx=1)
        start_row += 1

        self.lblAddress = Label(self, text="Addresse:")
        self.street = Entry(self, width=63)
        self.lblAddress.grid(row=start_row, column=0, sticky='w')
        start_row += 1
        self.street.grid(row=start_row, column=0, sticky='w', columnspan=maxColCount, padx=1)
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
        self.country.grid(row=start_row, column=0, sticky='w', columnspan=maxColCount, padx=1)
        start_row += 1

        self.btnChange = Button(self, text="Change", width=8)
        self.btnChange.grid(row=start_row, column=2, sticky='e')


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
        self.number = Spinbox(self, from_=0, to=1000000, wrap=True, increment=1)
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
        
        self.canvasFrame.bind("<Configure>", lambda e:self.scrollregion())#)self.canvas.configure(scrollregion=self.canvas.bbox("all")))

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
        
        # self.invoiceTotalPriceUnit = Entry(self, width=30)
        # self.invoiceTotalPrice = Entry(self, width=30)

        def clear(self):
            self.quantity.delete(0, 'end')
            self.unit.delete(0, 'end')
            self.description.delete(0, 'end')
            self.pricePerUnit.delete(0, 'end')
            # self.invoiceTotalPriceUnit.delete(0, 'end')
            self.unit.delete(0, 'end')


# View().mainloop()