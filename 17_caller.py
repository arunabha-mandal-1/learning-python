import area
print('I am in caller.py')
area.calculate_area(5,10)

# when we call function from other file, value of the __name__ is name of that particular module