from languages import python, java#, csharp, matlab, excel 
from source.parse_objects import Parser

class Decoder:
    selected_language = ""
    _lang = ""
    input = ""
    _output = []
    
    def __init__(self, input, language):
        self.input = input
        self.selected_language = language

    def __init__(self):
        self.langs = [python.Python(), java.Java()]
    
    def select_lang(self, obj):
        self._lang = obj
        self.selected_language = obj.to_string()
        return self.selected_language
    
    def input_data(self, input):
        self.input = input

    def filter_spaces(self,str): # Filters the spaces at the beginning or end of a string
        has_spaces = True
        while(has_spaces): 
            try:
                if(str.index(" ") == 0):
                    str = str[1:]
                elif(str.rindex(" ") == len(str)-1):
                    str = str[:len(str)-1]
                else:
                    has_spaces = False
            except ValueError:
                has_spaces = False
            
        return str


    def decode(self):
        lang = self._lang
        input = self.input
        output = self._output
        datatype = ""
        var_name = ""

        print(input)
        lhs = self.filter_spaces(input[0:input.index(lang.splitter)])
        rhs = self.filter_spaces(input[len(lhs)+1:])

        # Handle the left
        lhs = lhs.split(" ")
        if(lang.explicit_type == True):
            print(len(lhs))
            datatype = lhs[len(lhs)-2]
            var_name = lhs[len(len)-1]
        else:
            print(len(lhs))
            var_name = lhs[len(lhs)-1]


        output.append(datatype)     
        output.append(var_name)   
        # Handle the right

        # Gets rid of the opening bracket
        if(rhs[0] == lang.opener):
            rhs = rhs[1:]
            
            
            if(lang.line_end != ""):    # Checks the end of the string for a semicolon
                if(rhs[len(rhs)-1] == lang.line_end):
                    rhs=rhs[:len(rhs)-1]
                else:
                    rhs = rhs
                    print('err1',rhs)
                    #Throw error, incorrect syntax

            else:   # Language doesnt need a line end, we gucci
                rhs = rhs

            # Gets rid of closing bracket
            if(rhs[len(rhs)-1] == lang.closer):
                rhs=rhs[:len(rhs)-1]
            else:
                rhs=rhs
                print('err2',rhs)
                # Throw error, incorrect syntax

            objects = rhs.split(lang.row_deliminator)
            itms = []
            for obj in objects:
                itms.insert(0,self.filter_spaces(obj))


            parser = Parser(lang)

            if(datatype != ""): # We know the data type already!
                objects =parser.parse(itms, lang.type_to_string(datatype))
                #print(datatype)
            else:               # Data type not specific by decoded language, need to figure it out!
                objects =parser.parse(itms)
                output[0] = parser.datatype
                #print("dope")
            
            output.append(objects)

        else:
            print('An error has occurred somewhere?')

        print(output)
        return output



  