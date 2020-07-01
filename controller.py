import view
import model

class Controller():
    def __init__(self):
        # Variables
        self.path = ""
        self.company = {
            "name"      : "", 
            "street"    : "", 
            "number"    : "", 
            "postcode"  : "", 
            "location"  : "", 
            "country"   : "",
            "mail"      : "",
            "phone"     : "",
            "bank"      : "",
            "iban"      : "",
            "bic"       : ""
        }
        self.number = 0
        self.customer = []

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
        self.path = ""
        self.company = {
            "name"      : self.gui.companyName.get(), 
            "street"    : self.gui.companyStreet.get(),
            "number"    : self.gui.companyStreetNumber.get(),
            "postcode"  : self.gui.companyPostcode.get(),
            "location"  : self.gui.companyLocation.get(),
            "country"   : self.gui.companyCountry.get(),
            "mail"      : self.gui.companyMail.get(),
            "phone"     : self.gui.companyPhone.get(),
            "bank"      : self.gui.companyBank.get(),
            "iban"      : self.gui.companyIban.get(),
            "bic"       : self.gui.companyBic.get()
        }
        self.number = 0
        self.customer = []

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