# Working with JSON
# JSON = Javascript object notation
# Json is a data exchange format similar to XML
"""
JSON example
{
    "name":"tom",
    "address":"barite",
    "phone":526252225
}
"""
"""
XML example

<name>tom</name>
<address>barite</address>
<phone>526252225</phone>
"""
# JSON is lightweight format compared to XML. That's why JSON is gaining lot of populariry nowadays.
# There is no object called JSON in python, JSON is just a format implemented in different languages.
book={}
book['tom']={
    'name':'tom',
    'address':'24 bari',
    'phone':1234567890
}
book['bob']={
    'name':'bob',
    'address':'2 bari',
    'phone':9874563210
}

import json
s=json.dumps(book) # to convert in a JSON formatted string
print(s)
with open("E:\\codebasics-ml\\python\\15_my_json_1.txt", "w") as f:
    f.write(s)


# s=>string
phoneBook=json.loads(s) # phoneBook=>dict
# now we can use phoneBook as a dictionary
print(phoneBook['bob']['phone']) # checking