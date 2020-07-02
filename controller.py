import view
import model

class Controller():
    def __init__(self):
        # Initial Data
        self._getInitialData()
        self._setInitialView()

        # Objects
        self.model = model.Model()
        self.gui = view.View()

        # Update
        self._updateData()

        # GUI
        self._configView()
        self.gui.mainloop()

    def _getInitialData(self):
        print("Read Init File")

    def _writeInitFile(self):
        print("Write Init File")

    def _updateData(self):
        self.model.myCompany.company = self.gui.myCompany.name.get()
        self.model.myCompany.address = self.gui.myCompany.street.get()
        self.model.myCompany.postcode = self.gui.myCompany.postcode.get()
        self.model.myCompany.city = self.gui.myCompany.city.get()
        self.model.myCompany.mail = self.gui.myCompany.mail.get()
        self.model.myCompany.phone = self.gui.myCompany.phone.get()
        self.model.myCompany.bank = self.gui.myCompany.bank.get()
        self.model.myCompany.iban = self.gui.myCompany.iban.get()
        self.model.myCompany.bic = self.gui.myCompany.bic.get()


        self.path = ""
        self.number = 0

        self.model.myCustomer.company = self.gui.myCustomer.company.get()
        self.model.myCustomer.name1 = self.gui.myCustomer.name1.get()
        self.model.myCustomer.name2 = self.gui.myCustomer.name2.get()
        self.model.myCustomer.address = self.gui.myCustomer.street.get()
        self.model.myCustomer.postcode = self.gui.myCustomer.postcode.get()
        self.model.myCustomer.city = self.gui.myCustomer.city.get()
        self.model.myCustomer.country = self.gui.myCustomer.country.get()

    def _setInitialView(self):
        print("Set View")

    def _configView(self):
        print("Config View")
        self.gui.btnCreate.config(command=self.createInvoice)
        self.gui.btnChange.config(command=self.changeCustomer)

    def _readInputView(self):
        print("Read Input Data")
        self._updateData()

    def changeCustomer(self):
        print("Change customer")

    def _deleteCustomer(self):
        print("Delete customer not allowed")

    def createInvoice(self):
        print("Create Invoice")
        self._readInputView()
        _created = self.model.createInvoice()
        if not _created:
            return
        self._writeInitFile()

Controller()
