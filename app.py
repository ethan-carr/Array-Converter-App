from languages import python, java
from decoder import Decoder



test = 'String[] cars = {"Volvo", "BMW", "Ford", "Mazda"}; '


de = Decoder()
de.select_lang(java.Java())
de.input_data(test)
de.decode()
