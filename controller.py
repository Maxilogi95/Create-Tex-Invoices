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
            "country"   : ""
        }
        self.number = 0
        self.customer = []

        # Initial Data
        self._getInitialData()
        self._setInitialView()

        # Objects
        self.model = model.Model()
        self.gui = view.View()

        # GUI
        self.gui.mainloop()

    def _getInitialData(self):
        print("Read Init File")

    def _setInitialView(self):
        print("Set View")

    def _readInputView(self):
        print("Read Input Data")

    def _writeInitFile(self):
        print("Write Init File")

    def _isNewCustomer(self):
        print("Does customer exist?")
        _new = True
        return _new

    def _newCustomer(self):
        print("New customer")

    def changeCustomer(self):
        print("Change customer")

    def _deleteCustomer(self):
        print("Delete customer not allowed")

    def _isAllDataOk(self):
        print("Data ok? Filled?")
        _ok = True
        _ok = _ok and self.path != ""
        print("  Data is ok: " + str(_ok))
        return _ok

    def doCreateInvoice(self):
        print("Create Tex File with Input Data")

    def createInvoice(self):
        print("Create Invoice")
        _save = True
        self._readInputView()
        if not self._isAllDataOk():
            print("  Message Box: Trotzdem speichern?")
            _save = True # Rückgabe von Message Box

        if not _save:
            return

        if self._isNewCustomer():
            self._newCustomer()

        self._writeInitFile()

        self.doCreateInvoice()



Controller().createInvoice()