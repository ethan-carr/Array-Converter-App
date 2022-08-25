
import re


class Parser:
    _settings = []
    _lang = ""


    def __init__(self):
        self._default = '"'

    def __init__(self, lang):
        self._lang = lang

    def parse(self, itms):
        print("parsing without explicit datatype")
        return itms

    def parse(self, itms, datatype):
        lang = self._lang

        print("parsing with data type " + datatype)
    
        if datatype == "string":
            #Remove the beginning and ending characters
            for itm in itms:
                itm  = itm[1:len(itm)-2]

                return itms
        elif datatype == "int":
            # No formatting required?
            return itms
        elif datatype == "double":
            return itms
            # NRK
        elif datatype == "boolean":
            for itm in itms:
                if itm == lang.bools[0]:
                    itm = "true"
                elif itm == lang.bools[1]:
                    itm = "false"
        elif datatype == "char":
            for itm in itms:
                itm = itm[1:len(itm)-1]
        elif datatype == "object":
            return itms

        return itms

    