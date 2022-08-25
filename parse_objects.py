
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
        outs = []
        if datatype == "string":
            #print("STRING!")
            #Remove the beginning and ending characters
            for itm in itms:
                outs.append(itm[1:len(itm)-1])

        elif datatype == "int":
            outs = itms
        elif datatype == "double":
            outs = itms
        elif datatype == "boolean":
            for itm in itms:
                if itm == lang.bools[0]:
                    outs.append("true")
                elif itm == lang.bools[1]:
                    outs.append("false")
        elif datatype == "char":
            for itm in itms:
                outs.append(itm[1:len(itm)-1])
        elif datatype == "object":
            return itms

        return outs

    