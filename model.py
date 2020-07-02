class Model():
    def __init__(self):
        print("Model Init")
        self.path = ""
        self.myCustomer = Customer()
        self.myCompany = Company()
        self.myCustomerList = []
        self.chooseCustomerList = []

        self.msg = ""
        self.msgTitle = ""

    def _isNewCustomer(self, choosedCustomer=""):
        _new = choosedCustomer == ""
        return _new

    def _addCustomer(self):
        self.myCustomerList.append(self.myCustomer)

    def _createChooseCustomerList(self):
        for myCustomer in self.myCustomerList:
            self.chooseCustomerList.append(myCustomer.choose)

    def chooseCustomer(self, choosedCustomer=""):
        if choosedCustomer == "":
            return

        for myCustomer in self.myCustomerList:
            _id = myCustomer.choose[myCustomer.choose.find("(")+1 : myCustomer.choose.find(")")]
            
            if str(self.myCustomer.id) == str(_id):
                self.myCustomer = myCustomer

    def _isAllDataOk(self):
        _ok = False
        _ok = self._isCompanyDataOk() and self._isCustomerDataOk()
        return _ok

    def _isCustomerDataOk(self):
        _ok = False
        _okName = (
            self.myCustomer.company == "" and (self.myCustomer.name1 != "" and self.myCustomer.name2 != "")
            or 
            self.myCustomer.company != "" and (self.myCustomer.name1 == "" and self.myCustomer.name2 == "")
        )
        _okAddress = self.myCustomer.address != ""
        _okPostcode = self.myCustomer.postcode != ""
        _okCity = self.myCustomer.city != ""

        _ok = _okName and _okAddress and _okPostcode and _okCity
        return _ok

    def _isCompanyDataOk(self):
        _ok = False
        _okCompany = self.myCompany.company != ""
        _okAddress = self.myCompany.address != ""
        _okPostcode = self.myCompany.postcode != ""
        _okCity = self.myCompany.city != ""
        _okCountry = self.myCompany.country != ""
        _okMail = self.myCompany.mail != ""
        _okPhone = self.myCompany.phone != ""
        _okBank = self.myCompany.bank != ""
        _okIban = self.myCompany.iban != ""
        _okBic = self.myCompany.bic != ""

        _ok = _okCompany and _okAddress and _okPostcode and _okCity and _okCity and _okCompany and _okMail and _okPhone and _okBank and _okIban and _okBic
        return _ok

    def _doCreateInvoice(self):
        print("Create Tex File with Input Data")


    def createInvoice(self, choosedCustomer=""):
        _save = self._isAllDataOk()

        if not _save:
            print("  Message Box: " + self.msg + self.msgTitle)
            return _save

        if self._isNewCustomer(choosedCustomer):
            self._addCustomer()

        self._doCreateInvoice()

        return _save

    def calculateTotalUnitPrice(self, unit_count, price_per_unit):
        return unit_count * price_per_unit

    def totalizePrice(self, old_total_price, total_unit_price):
        return old_total_price + total_unit_price

    def _writeInitialFile(self):
        _content = ""

        _content += "# Path to initial file\n"
        _content += ""
        _content += "# Path to company logo"
        _content += ""
        _content += "# Path to invoices"
        _content += ""
        _content += "# Company data dictionary"
        _content += self._getAllCompanyData()
        _content += "# Last invoice number"
        _content += self._getLastInvoiceNumber()
        _content += "# Customer data dictionaries"
        _content += self._getAllCustomerData()

        with open('somefile.txt', 'w') as _file:
            _file.write(_content)

    def _getAllCompanyData(self):
        return ""

    def _getLastInvoiceNumber(self):
        return ""

    def _getAllCustomerData(self):
        return ""

class Customer():
    def __init__(self, id="", company="", name1="", name2="", address="", postcode="", city="", country=""):
        self.id = id
        self.company = company
        self.name1 = name1
        self.name2 = name2
        self.address = address
        self.postcode = postcode
        self.city = city
        self.country = country

        self.name = self.name2 + ", " + self.name1
        self.choose = self.name + " - " + self.company + " - " + self.city + " (" + str(self.id) + ")"

class Company():
    def __init__(self, company="", address="", postcode="", city="", country="", mail="", phone="", bank="", iban="", bic=""):
        self.company = company
        self.address = address
        self.postcode = postcode
        self.city = city
        self.country = country
        self.mail = mail
        self.phone = phone
        self.bank = bank
        self.iban = iban
        self.bic = bic
