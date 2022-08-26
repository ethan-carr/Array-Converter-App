from languages import python, java

class Encoder:
    _encoded_lang = ""
    _input = ""

    

    def __init__(self):
        self._encoded_lang = python.Python()
        

    def __init__(self, input, lang):
        self._input = input
        self._encoded_lang  = lang

    def set_language(self, lang):
        self._encoded_lang = lang

    def set_input(self, input):
        self._input = input

    def format_item(self, item, datatype):
        lang = self._encoded_lang
        out = ""
        if datatype=="string":
            out = lang.stringsep[0] + item + lang.stringsep[0]
        elif datatype == "char":
            out = lang.charsep + item + lang.charsep
        elif datatype == "boolean":
            if(item):
                out = lang.bools[0]
            else:
                out = lang.bools[1]
        else:
            return item
        
        return out
    

    def encode(self, input, lang):
        self._input = input
        self._encoded_lang = lang
        self.encode()
        


    def encode(self):
        input2 = self._input
        input = input2
        lang = self._encoded_lang
        #print(self._input, self._encoded_lang)
        #print(input)
        # Takes care of data type declaration (if req)
        output = ""
        datatype = input[0]

        if(lang.explicit_type == False):
            output+=""
            input.remove(input[0])
        else:
            output+=lang.string_to_type(input[0]) + " "
            input.remove(input[0])

        # Takes care of variable name
        output += input[0]
        input.remove(input[0])

        # Adding in equal sign
        output+=lang.splitter

        # Adds opener
        output+=lang.opener

        for inp in input[0]:
            # Everything goes into format item
            output += self.format_item(inp,datatype) + lang.row_deliminator

        # removes the extra comma
        output = output[0:len(output)-1]

        # Adds closer and line end
        output+=lang.closer + lang.line_end

        print(output)
        #self.encode(self._input, self._encoded_lang)

    
        