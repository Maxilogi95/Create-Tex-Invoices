#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import codecs


class Model():
    def __init__(self):
        print("Model Init")
        self.path = "Invoices.ini"

        self.myIni = InitialFile(path=self.path)
        self.myList = self.myIni.initList
        self.myCompany = self.myIni.initCompany
        self.myInvoice = self.myIni.initInvoice
        self.myTex = InvoiceTex()
        self.myCustomer = Customer()

        self.msg = ""
        self.msgTitle = ""

    def _isAllDataOk(self):
        _ok = False
        _ok = self.myCompany.isDataOk() and self.myCustomer.isDataOk()
        return _ok

    def createInvoice(self, choosedCustomer=""):
        _save = self._isAllDataOk()

        if not _save:
            print("  Message Box: " + self.msg + self.msgTitle)
            return _save

        if choosedCustomer == "":
            self.myList.addCustomer(self.myCustomer)
        else:
            self.myList.createChooseCustomerList()

        self.myIni.saveAllData(self.myCompany, self.myList.customerList, self.myInvoice)

        self.myInvoice.calculateTotalPrice()
        self.myTex.create(self.myCompany, self.myCustomer, self.myInvoice)

        return _save

    def onSelectCustomer(self, choosedCustomer):
        self.myCustomer = self.myList.getSelectedCustomer(choosedCustomer)

class List():
    """
    class List:
        The class will manage the customer lists with ...
            - ... Customer() objects
            - ... Choose Name of customer
    """
    def __init__(self):
        self.customerList = list()
        self.chooseCustomerList = list()

    def addCustomer(self, customer):
        """
        Description:
            Add a customer to the customerList. Increase the customer id, if customer do not have an id.
            Also create the choose name, if no one exist.
        Arguments:
            customer: Customer() object
        """
        if customer.id == "":
            customer.id = len(self.customerList) + 1
        if customer.choose == "":
            customer.createChooseName()

        self.customerList.append(customer)
        self.createChooseCustomerList()

    def createChooseCustomerList(self):
        """
        Description:
            Create the list of choose names. First, all choose names will be created from all customers,
            then the choose name will be append to the chooseCustomerList.
        """
        self.chooseCustomerList = ['']
        for customer in self.customerList:
            customer.createChooseName()
            self.chooseCustomerList.append(customer.choose)

    def getSelectedCustomer(self, choosedCustomer=""):
        """
        Description:
            Returns a specific Customer to the choose name.
            If choose name is "", then a new Customer object will be returned.
        Arguments:
            choosedCustomer = ""
        Return:
            Customer() object
        """
        if choosedCustomer == "":
            return Customer()

        for customer in self.customerList:
            _id = choosedCustomer[choosedCustomer.find("(")+1:choosedCustomer.find(")")]
            if str(customer.id) == str(_id):
                return customer

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
        ok = False
        okCompany = self.company != ""
        okAddress = self.address != ""
        okPostcode = self.postcode != ""
        okCity = self.city != ""
        okCountry = self.country != ""
        okMail = self.mail != ""
        okPhone = self.phone != ""
        okBank = self.bank != ""
        okIban = self.iban != ""
        okBic = self.bic != ""

        ok = (okCompany and okAddress and okPostcode and 
            okCity and okCountry and okCompany and 
            okMail and okPhone and okBank and 
            okIban and okBic)
        return ok


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
        self.config.read(self.path, encoding='utf-8')

        self.logo = ""

        # Data for Customer/Company/Invoice
        self.initList = List()
        self.initCompany = Company()
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

                self.initList.addCustomer(_customer)
        except Exception as ex:
            print(ex)
            return

    def saveAllData(self, company, customerList, invoice=None):
        self.setCompanyData(company)
        self.setInvoiceData(invoice)
        self.setCustomerData(customerList)

        with codecs.open(self.path, 'w', 'utf-8') as iniFile:
            self.config.write(iniFile)

    def setCompanyData(self, company):
        self.config['Company'] = {
            'Logo': self.logo,
            'Name': company.company,
            'Street': company.address,
            'Postcode': company.postcode,
            'City': company.city,
            'Country': company.country,
            'Mail': company.mail,
            'Phone': company.phone,
            'Bank': company.bank,
            'Iban': company.iban,
            'Bic': company.bic
        }

    def setInvoiceData(self, invoice):
        self.config['Invoice'] = {
            'Number': invoice.number,
            'Path': invoice.path
        }

    def setCustomerData(self, customerList):
        for customer in customerList:
            self.config['Customer' + str(customer.id)] = {
                'Id': customer.id,
                'Company': customer.company,
                'FirstName': customer.name1,
                'LastName': customer.name2,
                'Street': customer.address,
                'Postcode': customer.postcode,
                'City': customer.city,
                'Country': customer.country
            }


class InvoiceTex():
    def __init__(self, company=None, customer=None, invoice=None):
        self.company = company
        self.customer = customer
        self.invoice = invoice
        self.replaceDict = {}

    def create(self, company=None, customer=None, invoice=None):
        if self.company == None or self.customer == None or self.invoice == None:
            self.company = company
            self.customer = customer
            self.invoice = invoice

        self._fillData()
        template = codecs.open('template.tex', 'r', 'utf-8')
        _data = template.read()
        template.close()

        for key in self.replaceDict.keys():
            _data = _data.replace(key, str(self.replaceDict[key]))

        with codecs.open(str(self.invoice.number) + '.tex', 'w', 'utf-8') as template:
            template.write(_data)

    def _fillData(self):
        self.replaceDict = {
            # Company Data
            "<NAME>":       self.company.company,
            "<STREET>":     self.company.address,
            "<POSTCODE>":   self.company.postcode,
            "<CITY>":       self.company.city,
            "<PHONE>":      self.company.phone,
            "<MAIL>":       self.company.mail,
            "<IBAN>":       self.company.iban,
            "<BIC>":        self.company.bic,
            "<BANK>":       self.company.bank,
            # Customer Data
            "<CUSTOMERID>":         self.customer.id,
            "<CUSTOMERCOMPANY>":    self.customer.company,
            "<CUSTOMERNAME>":       self.customer.name1 + " " + self.customer.name2,
            "<CUSTOMERSTREET>":     self.customer.address,
            "<CUSTOMERPOSTCODE>":   self.customer.postcode,
            "<CUSTOMERCITY>":       self.customer.city,
            # Invoice Data
            "<INVOICENO>":  self.invoice.number,
            "<INVOICETITLE>": "",
            "<INVOICEDATA>": self._generateInvoiceData(),
            "<INVOICESUM>": self.invoice.totalPrice
        }

    def _generateInvoiceData(self):
        for part in self.invoice.invoiceList:
            print()
        return ""
