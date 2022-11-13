# Raise Exception And Finally => will have to give a deep dive

# try:
#     raise MemoryError ("memory error")# google "python built-in exceptions"
# except MemoryError as e:
#     print(e)

# Exceptions are classes in python
# To define my own exception, i need to define my own class
class Accident(Exception):
    # Accident is derived from Exception
    def __init__(self, msg):
        self.msg=msg
    def print_exception(self):
        print("User defined exception: ", self.msg)
    def handle(self):
        print("accident occured, take detour")

try:
    raise Accident("crash between two cars") # creating an exception here
except Accident as e:
    e.handle()



# finally keyword
def process_file():
    try:
        f=open("E:\\codebasics-ml\\python\\22_dummy.txt")
        x=1/0
    except FileNotFoundError as e:
        print("inside except")
        print(e)
    finally:
        print("cleaning up file")
        f.close()
        # No matter what it will execute code in finally block even if there is any error i try block


process_file()