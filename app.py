from languages import python, java
import Decoder



test = 'String[] cars = {"Volvo", "BMW", "Ford", "Mazda"}; '


de = Decoder()
de.select_lang(python.Python())
de.input_data(test)
de.decode()