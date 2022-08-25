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

    def encode(self, input, lang):
        print("encoding!")
        





    def encode(self):
        input = self._input
        lang = self._encoded_lang
        #print(self._input, self._encoded_lang)
        
        # Takes care of data type declaration (if req)
        output = ""
        if(lang.explicit_type == False):
            output+=""
            input.remove(input[0])
        else:
            output+=input[0]
            input.remove(input[0])

        # Takes care of variable name
        output += input[0]
        input.remove(input[0])

        # Adding in equal sign
        output+=lang.splitter

        # Adds opener
        output+=lang.opener

        for inp in input[0]:
            
            # oops this doesnt work! need to encode as the datatype
            output+=inp + lang.row_deliminator

        # removes the extra comma
        output = output[0:len(output)-1]

        # Adds closer and line end
        output+=lang.closer + lang.line_end

        print(output)
        #self.encode(self._input, self._encoded_lang)

    