# what is __name__=="__main__"  in python

def calculate_area(base, height):
    print('__name__:', __name__)
    return 0.5*base*height

# If we run this file directly(not from other file), __name__ will be set in __main__
if __name__=="__main__":
    print('I am in area.py')
    a=calculate_area(10,20)
    print("Area :", a)
else:
    print("Not called directly.")