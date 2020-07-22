#!/usr/bin/env python
# -*- coding: utf-8 -*-

import view
import model


class Controller():
    def __init__(self):
        # Objects
        self.model = model.Model()
        self.gui = view.View()

        # Update
        self._setInitialView()
        self._updateData()

        # GUI
        self._configView()
        self.gui.mainloop()

    def _setInitialView(self):
        self.gui.myCompany.name.insert(0, self.model.myCompany.company)
        self.gui.myCompany.street.insert(0, self.model.myCompany.address)
        self.gui.myCompany.postcode.insert(0, self.model.myCompany.postcode)
        self.gui.myCompany.city.insert(0, self.model.myCompany.city)
        self.gui.myCompany.country.insert(0, self.model.myCompany.country)
        self.gui.myCompany.mail.insert(0, self.model.myCompany.mail)
        self.gui.myCompany.phone.insert(0, self.model.myCompany.phone)
        self.gui.myCompany.bank.insert(0, self.model.myCompany.bank)
        self.gui.myCompany.iban.insert(0, self.model.myCompany.iban)
        self.gui.myCompany.bic.insert(0, self.model.myCompany.bic)

        # Update invoice number and choose name(s)
        self._updateGUI()

    def onSelectCustomer(self):
        self.model.onSelectCustomer(self.gui.myCustomer.choose.get())

        self.gui.myCustomer.editable(True)
        self.gui.myCustomer.company.delete(0, 'end')
        self.gui.myCustomer.form.delete(0, 'end')
        self.gui.myCustomer.title.delete(0, 'end')
        self.gui.myCustomer.name1.delete(0, 'end')
        self.gui.myCustomer.name2.delete(0, 'end')
        self.gui.myCustomer.street.delete(0, 'end')
        self.gui.myCustomer.postcode.delete(0, 'end')
        self.gui.myCustomer.city.delete(0, 'end')
        self.gui.myCustomer.country.delete(0, 'end')

        if self.gui.myCustomer.choose.get() != "":
            self.gui.myCustomer.company.insert(0, self.model.myCustomer.company)
            self.gui.myCustomer.form.insert(0, self.model.myCustomer.form)
            self.gui.myCustomer.title.insert(0, self.model.myCustomer.title)
            self.gui.myCustomer.name1.insert(0, self.model.myCustomer.name1)
            self.gui.myCustomer.name2.insert(0, self.model.myCustomer.name2)
            self.gui.myCustomer.street.insert(0, self.model.myCustomer.address)
            self.gui.myCustomer.postcode.insert(0, self.model.myCustomer.postcode)
            self.gui.myCustomer.city.insert(0, self.model.myCustomer.city)
            self.gui.myCustomer.country.insert(0, self.model.myCustomer.country)
            self.gui.myCustomer.editable(False)

    def _updateCompanyData(self):
        self.model.myCompany.company = self.gui.myCompany.name.get()
        self.model.myCompany.address = self.gui.myCompany.street.get()
        self.model.myCompany.postcode = self.gui.myCompany.postcode.get()
        self.model.myCompany.city = self.gui.myCompany.city.get()
        self.model.myCompany.country = self.gui.myCompany.country.get()
        self.model.myCompany.mail = self.gui.myCompany.mail.get()
        self.model.myCompany.phone = self.gui.myCompany.phone.get()
        self.model.myCompany.bank = self.gui.myCompany.bank.get()
        self.model.myCompany.iban = self.gui.myCompany.iban.get()
        self.model.myCompany.bic = self.gui.myCompany.bic.get()

    def _updateCustomerData(self):
        self.model.myCustomer.choose = self.gui.myCustomer.choose.get()
        self.model.myCustomer.company = self.gui.myCustomer.company.get()
        self.model.myCustomer.form = self.gui.myCustomer.form.get()
        self.model.myCustomer.title = self.gui.myCustomer.title.get()
        self.model.myCustomer.name1 = self.gui.myCustomer.name1.get()
        self.model.myCustomer.name2 = self.gui.myCustomer.name2.get()
        self.model.myCustomer.address = self.gui.myCustomer.street.get()
        self.model.myCustomer.postcode = self.gui.myCustomer.postcode.get()
        self.model.myCustomer.city = self.gui.myCustomer.city.get()
        self.model.myCustomer.country = self.gui.myCustomer.country.get()

        self.gui.myCustomer.choose['values'] = self.model.myList.chooseCustomerList

    def _updateInvoiceData(self):
        _i = 0
        for _part in self.gui.myInvoice.partList:
            self.model.myInvoice.invoiceList[_i].quantity = _part.quantity.get()
            self.model.myInvoice.invoiceList[_i].unit = _part.unit.get()
            self.model.myInvoice.invoiceList[_i].description = _part.description.get()
            self.model.myInvoice.invoiceList[_i].unit_price = _part.pricePerUnit.get()
            _i += 1

    def _updateData(self):
        self._updateCustomerData()
        self._updateCompanyData()
        self._updateInvoiceData()

    def _updateGUI(self, isCreated=True):
        if not isCreated:
            self.gui.myCustomer.editable(True)
            return

        # Update invoice number
        self.gui.myInvoice.number.config(state='normal')
        self.gui.myInvoice.number.delete(0, 'end')
        self.gui.myInvoice.number.insert(0, int(self.model.myInvoice.number)+1)
        self.gui.myInvoice.number.config(state='disabled')

        # Update customer list in VIEW
        self.gui.myCustomer.sort.set(2)
        self.gui.myCustomer.choose['values'] = self.model.myList.chooseCustomerList
        self.gui.myCustomer.choose.set(self.model.myCustomer.choose)

    def _configView(self):
        print("Config View")
        # Customer
        self.gui.myCustomer.btnChange.config(command=lambda: self.gui.myCustomer.editable(True))
        self.gui.myCustomer.choose.bind('<<ComboboxSelected>>', lambda f: self.onSelectCustomer())
        self.gui.myCustomer.form.config(values=['', 'Frau', 'Herr'], state='readonly')
        self.gui.myCustomer.rdbName2.config(command=lambda:
            self.model.myList.sortChooseCustomerList(self.gui.myCustomer.sort.get())
            )
        self.gui.myCustomer.rdbCompany.config(command=lambda:
            self.model.myList.sortChooseCustomerList(self.gui.myCustomer.sort.get())
            )
        self.gui.myCustomer.rdbNumber.config(command=lambda:
            self.model.myList.sortChooseCustomerList(self.gui.myCustomer.sort.get())
            )
        # Company

        # Invoice
        self.gui.myInvoice.btnAdd.config(command=lambda: (
            self.gui.myInvoice.addPart(),
            self.model.myInvoice.addNewInvoicePart()
            ))
        # Other GUI components
        self.gui.btnCreate.config(command=self.createInvoice)
        self.gui.btnClose.config(command=self.quit)

    def createInvoice(self):
        self.gui.myCustomer.editable(False)
        # Get data from VIEW and set data in MODEL
        self._updateData()

        # Create invoice with all updated data
        _created = self.model.createInvoice(self.gui.myCustomer.choose.get())

        # Update GUI
        self._updateGUI(isCreated=_created)

    def quit(self):
        self.gui.destroy()


Controller()
