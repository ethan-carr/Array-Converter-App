import random
import string


# Global Variables (changes settings for all tests)
array_items = 5


# Create a test array of INTEGERS
items_length = 5
#
int_arr = []
item = ""
for i in range(array_items):
    for j in range(items_length):
        item +=str(random.randint(0,9))
    int_arr.append(item)
    item = ""

#print(int_arr)


# Create a test array of DOUBLES
items_length = 10
var_name = "dubs"
#
double_arr = []
item = ""
for i in range(array_items):
    leading = random.randint(1,items_length/2)
    for i in range(leading):
        item +=str(random.randint(0,9))
    item += "."
    for i in range(items_length-leading):
        item +=str(random.randint(0,9))
    double_arr.append(item)
    item = ""

double_test = ["double",var_name,double_arr]
#print(double_test)


# Create a test array of STRINGS
items_length = 10
var_name = "strss"
#
str_arr = []
item = ""
for i in range(array_items):
    for j in range(items_length):
        item +=random.choice(string.ascii_letters)
        #item+=chr(random.randint(101, (101+26)))
    str_arr.append('"' + item + '"')
    item = ""
    
string_test = ["string",var_name,str_arr]
#print(string_test)


# Create a test array of CHARS
items_length = 1
var_name = "chss"
#
char_arr = []
item = ""
for i in range(array_items):
    for j in range(items_length):
        item +=random.choice(string.ascii_letters)
        #item+=chr(random.randint(101, (101+26)))
    char_arr.append("'" + item + "'")
    item = ""
    
char_test =["char",var_name,char_arr]
#print(char_test)


# Create a test array of BOOLEANS
items_length = 1
var_name = "boold"
#
bool_arr = []
item = ""
for i in range(array_items):
    for j in range(items_length):
        item =bool(random.randint(0,1))
    bool_arr.append(item)
    item = ""

bool_test = ["boolean",var_name,bool_arr]
#print(bool_test)
