from doctest import OutputChecker
from languages import python, java#, csharp, matlab, excel 

# Sets up the supoprted languages

langs = [python.Python(), java.Java()]#, csharp.CSharp(), matlab.MATLAB(), excel.Excel()]

# Couple worker functions :P

def filter_spaces(str): # Filters the spaces at the beginning or end of a string
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







lang = python.Python()




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

    def decode(self):
        lang = self._lang
        output = self._output

        left = filter_spaces(test[0:test.index(lang.splitter)])
        right = filter_spaces(test[len(left)+2:])
        print(left, right)




        return output



    
    

