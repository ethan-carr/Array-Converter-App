
class CSharp:
    def __init__(self):
        self.explicit_type = True
        self.splitter = "=" 
        self.opener = "["
        self.closer = "]"
        self.stringsep = ['"'] 
        self.charsep = "'"
        self.line_end = ";"  
        self.row_deliminator = ","
        self.row_ender = ";"
        self.bools = ["true", "false"]
        
    def to_string(self):
        return "CSharp"
    
    def type_to_string(self, str):
        # Interpreted languages do not need anything in here, as its only referenced if explicit_type == true
        #return str
        
        if(str == "string[]"):
            return "string"
        elif(str == "int[]"):
            return "int"
        elif(str == "double[]"):
            return "double"
        elif(str == "bool[]"):
            return "boolean"
        elif(str == "char[]"):
            return "char"
        #elif(str == "byte[]"):
        #    return "byte"
        else:
            return("object")

    def string_to_type(self, str):
        # Interpreted languages do not need anything in here, as its only referenced if explicit_type == true
        return str

        if(str == "string"):
            return "string[]"
        elif(str == "int"):
            return "int[]"
        elif(str == "double"):
            return "double[]"
        elif(str == "boolean"):
            return "bool[]"
        elif(str == "char"):
            return "char[]"
        #elif(str == "byte[]"): # not yet lol
        #    return "byte"
        else:
            return("object[]")