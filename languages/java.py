
class Java:
    def __init__(self):
        self.datatype = ""  # not necessary
        self.explicit_type = True
        #self.var_name = "" will be handled by the decoder
        self.splitter = "=" 
        self.opener = "{"
        self.closer = "}"
        self.stringsep = ["'", '"'] # Python can take either, hell for nesting
        self.line_end = ";"    # not necessary
        self.row_deliminator = ","
        self.row_ender = ";"

        self.bools = ["true", "false"]
        
    def to_string(self):
        return "Java"
    
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

    def string_to_type(self, str):
        return ""