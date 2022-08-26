
class Java:
    def __init__(self):
        self.explicit_type = True
        self.splitter = "=" 
        self.opener = "{"
        self.closer = "}"
        self.stringsep = ['"'] 
        self.charsep = "'"
        self.line_end = ";"  
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
        if(str == "string"):
            return "String[]"
        elif(str == "int"):
            return "int[]"
        elif(str == "double"):
            return "double[]"
        elif(str == "boolean"):
            return "boolean[]"
        elif(str == "char"):
            return "char[]"
        #elif(str == "byte[]"): # not yet lol
        #    return "byte"
        else:
            return("Object[]")