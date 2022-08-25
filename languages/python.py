
class Python:
    def __init__(self):
        self.datatype = ""  # not necessary
        self.explicit_type = False
        #self.var_name = "" will be handled by the decoder
        self.splitter = "=" 
        self.opener = "["
        self.closer = "]"
        self.stringsep = ["'", '"'] # Python can take either, hell for nesting
        self.charsep = "'"
        
        
        self.line_end = ""    # not necessary
        self.row_deliminator = ","
        self.row_ender = ";"

    def to_string(self):
        return "Python"

    def type_to_string(self, str):
        if(str == "String[]"):
            return "string"
        elif(str == "int[]"):
            return "int"
        elif(str == "double[]"):
            return "double"
        elif(str == "boolean[]"):
            return "boolean"
        elif(str == "char[]"):
            return "char"
        #elif(str == "byte[]"):
        #    return "byte"
        else:
            return("object")