class Model():
    def __init__(self):
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
    
    def _isNewCustomer(self):
        print("Does customer exist?")
        _new = True
        return _new

    def _newCustomer(self):
        print("New customer")

    def _isAllDataOk(self):
        print("Data ok? Filled?")
        _ok = True
        _ok = _ok and self.path != ""
        print("  Data is ok: " + str(_ok))
        return _ok

    def _doCreateInvoice(self):
        print("Create Tex File with Input Data")


    def createInvoice(self):
        _save = True
        if not self._isAllDataOk():
            print("  Message Box: Trotzdem speichern?")
            _save = True # Rückgabe von Message Box

        if not _save:
            return _save

        if self._isNewCustomer():
            self._newCustomer()

        self._doCreateInvoice()

        return _save

    def calculateTotalUnitPrice(self, unit_count, price_per_unit):
        return unit_count * price_per_unit

    def totalizePrice(self, old_total_price, total_unit_price):
        return old_total_price + total_unit_price
