
class Python:
    def __init__(self):
        self.datatype = ""  # not necessary
        #self.var_name = "" will be handled by the decoder
        self.splitter = "=" 
        self.opener = "["
        self.closer = "]"
        self.stringsep = ["'", '"'] # Python can take either, hell for nesting
        self.closer = ""    # not necessary
        self.row_deliminator = ","
        self.row_ender = ";"

        return self

 