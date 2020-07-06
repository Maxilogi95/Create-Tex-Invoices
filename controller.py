import view
import model

class Controller():
    def __init__(self):
        # Initial Data
        self._setInitialView()

        # Objects
        self.model = model.Model()
        self.gui = view.View()

        # Update
        self._updateInitialView()
        self._updateData()

        # GUI
        self._configView()
        self.gui.mainloop()

    def _updateInitialView(self):
        print("Read Init File")
        self.gui.myCustomer.choose['values'] = self.model.chooseCustomerList

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

    def _writeInitFile(self):
        print("Write Init File")

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
        self.model.myCustomer.name1 = self.gui.myCustomer.name1.get()
        self.model.myCustomer.name2 = self.gui.myCustomer.name2.get()
        self.model.myCustomer.address = self.gui.myCustomer.street.get()
        self.model.myCustomer.postcode = self.gui.myCustomer.postcode.get()
        self.model.myCustomer.city = self.gui.myCustomer.city.get()
        self.model.myCustomer.country = self.gui.myCustomer.country.get()

    def _updateInvoiceData(self):
        self.model.myInvoice.number = self.gui.myInvoice.number.get()
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

        self.path = ""
        self.number = 0

    def _setInitialView(self):
        print("Set View")

    def _configView(self):
        print("Config View")
        self.gui.btnCreate.config(command=self.createInvoice)
        self.gui.myCustomer.btnChange.config(command=self.changeCustomer)
        self.gui.myInvoice.btnAdd.config(command=lambda:(
            self.gui.myInvoice.addPart(),
            self.model.myInvoice.addNewInvoicePart()
            ))
        self.gui.myCustomer.choose.config(values=[''])
        self.gui.btnClose.config(command=self.quit)

    def changeCustomer(self):
        print("Change customer")

    def _deleteCustomer(self):
        print("Delete customer not allowed")

    def createInvoice(self):
        print("Create Invoice")
        self._updateData()
        _created = self.model.createInvoice()
        if not _created:
            return
        self._writeInitFile()

    def quit(self):
        self.model.myIni.saveAllData(self.model.myCompany, self.model.myCustomerList, self.model.myInvoice)
        self.gui.destroy()

Controller()
