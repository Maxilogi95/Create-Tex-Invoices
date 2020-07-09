import configparser
import json

class Model():
    def __init__(self):
        print("Model Init")
        self.path = "Invoices.ini"
        self.myIni = InitialFile(path=self.path)
        self.myCompany = self.myIni.initCompany
        self.myInvoice = self.myIni.initInvoice
        self.myCustomerList = self.myIni.initCustomerList
        self.chooseCustomerList = self.myIni.initChooseCustomerList
        self.myCustomer = Customer()
        

        self.msg = ""
        self.msgTitle = ""

    def _isNewCustomer(self, choosedCustomer=""):
        _new = choosedCustomer == ""
        return _new

    def _addCustomer(self):
        self.myCustomer.id = len(self.myCustomerList) + 1
        self.myCustomer.createChooseName()
        self.myCustomerList.append(self.myCustomer)
        self.createChooseCustomerList()

    def createChooseCustomerList(self):
        self.chooseCustomerList = ['']
        for myCustomer in self.myCustomerList:
            self.chooseCustomerList.append(myCustomer.choose)

    def chooseCustomer(self, choosedCustomer=""):
        if choosedCustomer == "":
            return

        for myCustomer in self.myCustomerList:
            _id = choosedCustomer[choosedCustomer.find("(")+1 : choosedCustomer.find(")")]
            print("Compare: " + str(myCustomer.id) + "==" + str(_id))
            if str(myCustomer.id) == str(_id):
                self.myCustomer = myCustomer
                return

    def _isAllDataOk(self):
        _ok = False
        _ok = self.myCompany.isDataOk() and self.myCustomer.isDataOk()
        return _ok

    def _doCreateInvoice(self):
        print("Create Tex File with Input Data")
        # Here I should have all valid data
        # Company
        print(self.myCompany.company)
        print(self.myCompany.address)
        print(self.myCompany.postcode)
        print(self.myCompany.city)
        print(self.myCompany.country)
        print(self.myCompany.mail)
        print(self.myCompany.phone)
        print(self.myCompany.bank)
        print(self.myCompany.iban)
        print(self.myCompany.bic)
        # Customer
        print(self.myCustomer.choose)
        print(self.myCustomer.company)
        print(self.myCustomer.name1)
        print(self.myCustomer.name2)
        print(self.myCustomer.address)
        print(self.myCustomer.postcode)
        print(self.myCustomer.city)
        print(self.myCustomer.country)
        # Invoice
        self.myInvoice.calculateTotalPrice()

    def createInvoice(self, choosedCustomer=""):
        _save = self._isAllDataOk()

        if not _save:
            print("  Message Box: " + self.msg + self.msgTitle)
            return _save

        if self._isNewCustomer(choosedCustomer):
            self._addCustomer()
            self.myIni.saveAllData(self.myCompany, self.myCustomerList, self.myInvoice)

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

        self.createChooseName()

    def createChooseName(self):
        _name = ""
        if self.name1 != "" and self.name2 != "":
            _name = self.name2 + ", " + self.name1 + " - " 
        _company = ""
        if self.company != "":
            _company = self.company + " - " 
        
        self.choose = _name + _company + self.city + " (" + str(self.id) + ")"

    def isDataOk(self):
        _ok = False
        _okName = (
            self.company != "" or (self.name1 != "" and self.name2 != "")
            #self.company == "" and (self.name1 != "" and self.name2 != "")
            #or 
            #self.company != "" and (self.name1 == "" and self.name2 == "")
            #or
            #self.company != "" and (self.name1 != "" and self.name2 != "")
        )
        _okAddress = self.address != ""
        _okPostcode = self.postcode != ""
        _okCity = self.city != ""

        _ok = _okName and _okAddress and _okPostcode and _okCity
        print("Customer data: " + str(_ok))
        return _ok

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
    
    def isDataOk(self):
        _ok = False
        _okCompany = self.company != ""
        _okAddress = self.address != ""
        _okPostcode = self.postcode != ""
        _okCity = self.city != ""
        _okCountry = self.country != ""
        _okMail = self.mail != ""
        _okPhone = self.phone != ""
        _okBank = self.bank != ""
        _okIban = self.iban != ""
        _okBic = self.bic != ""

        _ok = _okCompany and _okAddress and _okPostcode and _okCity and _okCity and _okCompany and _okMail and _okPhone and _okBank and _okIban and _okBic
        print("Company data: " + str(_ok))
        return _ok

class Invoice():
    def __init__(self, number=0, path=""):
        self.number = int(number)
        self.path = path
        self.invoiceList = []
        self.totalPrice = 0

        self.addNewInvoicePart()

    def addNewInvoicePart(self):
        self.invoiceList.append(self.Part())

    def calculateTotalPrice(self):
        self.totalPrice = 0
        for _invoice_part in self.invoiceList:
            _invoice_part.calculate()
            self.totalPrice += _invoice_part.total_unit_price

        print("Total Price: " + str(self.totalPrice))
            
    class Part():
        def __init__(self, quantity="", unit="", description="", unit_price=""):
            self.quantity = quantity
            self.unit = unit
            self.description = description
            self.unit_price = unit_price
            self.total_unit_price = 0

            self.valid = True

        def calculate(self):
            self.total_unit_price = 0
            if self.isEmpty():
                return
            try:
                self.total_unit_price = float(self.quantity) * float(self.unit_price)
            except Exception as ex:
                print(ex)
                self.valid = False

        def isEmpty(self):
            _empty = True
            _empty = _empty and self.quantity == ""
            _empty = _empty and self.unit == ""
            _empty = _empty and self.description == ""
            _empty = _empty and self.unit_price == "" 
            return _empty

class InitialFile():
    def __init__(self, path="Invoices.ini"):
        self.path = path
        self.config = configparser.ConfigParser()
        self.config.read(self.path)

        self.logo = ""

        # Data for Customer/Company/Invoice
        self.initCompany = Company()
        self.initCustomerList = []
        self.initChooseCustomerList = []
        self.initInvoice = Invoice()

        self.getAllData()

    def getAllData(self):
        self.getCompanyData()
        self.getInvoiceData()
        self.getCustomerData()

    def getCompanyData(self):
        try:
            self.logo = self.config.get('Company', 'Logo')
            self.initCompany.company = self.config.get('Company', 'Name')
            self.initCompany.address = self.config.get('Company', 'Street')
            self.initCompany.postcode = self.config.get('Company', 'Postcode')
            self.initCompany.city = self.config.get('Company', 'City')
            self.initCompany.country = self.config.get('Company', 'Country')
            self.initCompany.mail = self.config.get('Company', 'Mail')
            self.initCompany.phone = self.config.get('Company', 'Phone')
            self.initCompany.bank = self.config.get('Company', 'Bank')
            self.initCompany.iban = self.config.get('Company', 'Iban')
            self.initCompany.bic = self.config.get('Company', 'Bic')
        except Exception as ex:
            print(ex)
            return

    def getInvoiceData(self):
        try:
            self.initInvoice.number = self.config.get('Invoice', 'Number')
            self.initInvoice.path = self.config.get('Invoice', 'Path')
        except Exception as ex:
            print(ex)
            return

    def getCustomerData(self):
        try:
            _sections = self.config.sections()
            _customerSections = []
            for _section in _sections:
                if "Customer" in _section:
                    _customerSections.append(_section)

            for _section in _customerSections:
                _customer = Customer()
                _customer.id = self.config.get(_section, 'Id')
                _customer.company = self.config.get(_section, 'Company')
                _customer.name1 = self.config.get(_section, 'FirstName')
                _customer.name2 = self.config.get(_section, 'LastName')
                _customer.address = self.config.get(_section, 'Street')
                _customer.postcode = self.config.get(_section, 'Postcode')
                _customer.city = self.config.get(_section, 'City')
                _customer.country = self.config.get(_section, 'Country')
                _customer.createChooseName()

                self.initChooseCustomerList.append(_customer.choose)
                self.initCustomerList.append(_customer)
        except Exception as ex:
            print(ex)
            return

    def saveAllData(self, company, customerList, invoice=None):
        self.setCompanyData(company)
        self.setInvoiceData(invoice)
        self.setCustomerData(customerList)

        with open(self.path, 'w') as iniFile:
            self.config.write(iniFile)

    def setCompanyData(self, company):
        self.config['Company'] = {
            'Logo' : self.logo,
            'Name' : company.company,
            'Street' : company.address,
            'Postcode' : company.postcode,
            'City' : company.city,
            'Country' : company.country,
            'Mail' : company.mail,
            'Phone' : company.phone,
            'Bank' : company.bank,
            'Iban' : company.iban,
            'Bic' : company.bic
        }

    def setInvoiceData(self, invoice):
        self.config['Invoice'] = {
            'Number' : invoice.number,
            'Path' : invoice.path
        }

    def setCustomerData(self, customerList):
        for customer in customerList:
            self.config['Customer' + str(customer.id)] = {
                'Id' : customer.id,
                'Company' : customer.company,
                'FirstName' : customer.name1,
                'LastName' : customer.name2,
                'Street' : customer.address,
                'Postcode' : customer.postcode,
                'City' : customer.city,
                'Country' : customer.country
            }
