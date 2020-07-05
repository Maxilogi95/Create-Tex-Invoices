import json

class Model():
    def __init__(self):
        print("Model Init")
        self.path = ""
        self.myCustomer = Customer()
        self.myCompany = Company()
        self.myInvoice = Invoice()
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
    def __init__(self, number=0):
        self.number = int(number)
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
    def __init__(self, path):
        self.path = path

        self.logo = ""
        self.company = ""
        self.number = ""
        self.savePath = ""
        self.customers = ""

        # Data for Customer/Company/Invoice
        self.initCompany = Company()
        self.initCustomerList = []
        self.initInvoiceNumber = 0

    def load(self):
        _tmp = ""
        _flagLogo = False
        _flagCompany = False
        _flagNumber = False
        _flagPath = False
        _flagCustomer = False

        _iniLine = ["Logo_File_Path=", "Company=", "Number=", "Invoice_Path=", "Customers="]
        _iniFlags = [_flagLogo, _flagCompany, _flagNumber, _flagPath, _flagCustomer]
        _iniData = [self.logo, self.company, self.number, self.path, self.customers]

        _iniLength = len(_iniLine)

        with open(self.path, 'r') as file:
            for line in file:
                if line.find('#') == 0 or line.find('\n') == 0:
                    continue

                for i in range(_iniLength):
                    if line.find(_iniLine[i]) or _iniFlags[i]:
                        if not _iniFlags[i]:
                            _iniData[i] += line[len(_iniLine[i]):].replace('\n', '').replace(';', '')
                        else:
                            _iniData[i] += line.replace('\n', '').replace(';', '')
                        _iniFlags[i] = True
                '''
                if line.find("Logo_File_Path=") >= 0 or _flagLogo:
                    if not _flagLogo:
                        self.logo += line[len("Logo_File_Path="):].replace('\n', '')
                    else:
                        self.logo += line.replace('\n', '')
                    print("Logo File Path")
                    _flagLogo = True
                elif line.find("Company=") >= 0 or _flagCompany:
                    _flagCompany = True
                    print("Company")
                elif line.find("Number=") >= 0 or _flagNumber:
                    _flagNumber = True
                    print("Number")
                elif line.find("Invoice_Path=") >= 0 or _flagPath:
                    _flagPath = True
                    print("Invoice Path")
                elif line.find("Customers=") >= 0 or _flagCustomer:
                    _flagCustomer = True
                    print("Customers")
                '''
                if line.find(';') == 0:
                    _flagLogo = False
                    _flagCompany = False
                    _flagNumber = False
                    _flagPath = False
                    _flagCustomer = False


    def save(self):
        self._generateAllIniData()
        with open(self.path, 'w') as file:
            file.write(self.logo + self.company + self.number + self.savePath + self.customers)

    def _generateAllIniData(self):
        self._generateLogo()
        self._generateCompany()
        self._generateNumber()
        self._generateSavePath()
        self._generateCustomers()

    def _generateLogo(self):
        self.logo = "# Logo\n" + self.logo + ";\n"
    def _generateCompany(self):
        self.company = "# Firma\n" + self.company + ";\n"
    def _generateNumber(self):
        self.number = "# Letzte Rechnungsnummer\n" + self.number + ";\n"
    def _generateSavePath(self):
        self.savePath = "# Speicherort der Rechnungen\n" + self.savePath + ";\n"
    def _generateCustomers(self):
        self.customers = "# Kunden\n" + self.customers + ";\n"

    def getInitCompanyData(self):
        _companyDict = json.loads(self.company)

        self.initCompany.company = _companyDict['name']
        self.initCompany.address = _companyDict['street']
        self.initCompany.postcode = _companyDict['postcode']
        self.initCompany.city = _companyDict['city']
        self.initCompany.country = _companyDict['country']
        self.initCompany.mail = _companyDict['mail']
        self.initCompany.phone = _companyDict['phone']
        self.initCompany.iban = _companyDict['iban']
        self.initCompany.bic = _companyDict['bic']

        return self.initCompany

    def getInitCustomerDataList(self):
        _customerList = json.loads(self.customers)
        for _customerDict in _customerList:
            _customer = Customer()
            _customer.id = _customerDict['id']
            _customer.company = _customerDict['company']
            _customer.name1 = _customerDict['name1']
            _customer.name2 = _customerDict['name2']
            _customer.address = _customerDict['street']
            _customer.postcode = _customerDict['postcode']
            _customer.city = _customerDict['city']
            _customer.country = _customerDict['country']

            self.initCustomerList.append(_customer)
        
        return self.initCustomerList

    def getInitInvoiceData(self):
        return self.initInvoiceNumber
