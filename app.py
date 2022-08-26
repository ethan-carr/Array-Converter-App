from languages import python, java
from source.decoder import Decoder
from source.encoder import Encoder



#test = 'String[] cars = {"Volvo", "BMW", "Ford", "Mazda"}; '
test = "cars=['Mazda','Ford','BMW','Volvo']"

de = Decoder()
#de.select_lang(java.Java())
de.select_lang(python.Python())
de.input_data(test)
output =de.decode()
#en = Encoder(output, python.Python())
en = Encoder(output, java.Java())
en.encode()
