

class Parser:
    _settings = []
    _lang = ""
    datatype = ""

    def __init__(self):
        self._default = '"'

    def __init__(self, lang):
        self._lang = lang
    

    def parse(self, itms, datatype):
        lang = self._lang

        print("parsing with data type " + datatype)
        outs
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

    def parse(self, itms):
        lang = self._lang
        datatype = self.datatype
        print("parsing without explicit datatype")

        # Need to parse the data ourselves and determine what kinda data type
        
        outs = []
        for itm in itms:
            is_num = False
            is_str = False
            is_bool = False


            try:
                int(itm)
                is_num = True
            except ValueError:
                is_num = False
            
            temp_type = ""
            if(itm[0] in lang.stringsep):
                if(len(itm) == 1):
                    temp_type = "char"
                    
                else:
                    temp_type = "string"
                    
                outs.append(itm[1:len(itm)-1])
            elif(itm in lang.bools):
                temp_type = "boolean"
                if itm == lang.bools[0]:
                    outs.append("true")
                elif itm == lang.bools[1]:
                    outs.append("false")
                
            elif(is_num):
                if(float(itm) % 1 == 0):
                    temp_type = "int"
                    outs.append(itm)
                else:
                    temp_type = "double"
                    outs.append(itm)
            else:
                temp_type = "object"
                outs.append(itm)

            print(temp_type)

            # Handle superceeding here

            self.datatype =temp_type
                



        return outs