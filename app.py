from languages import python, java
from decoder import Decoder
from encoder import Encoder



test = 'String[] cars = {"Volvo", "BMW", "Ford", "Mazda"}; '


de = Decoder()
de.select_lang(java.Java())
de.input_data(test)
output =de.decode()
en = Encoder(output, python.Python())
en.encode()
