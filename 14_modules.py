# Modules in Python
# the whole idea of "reuse" applies to programming world as well
# modules is a way to reuse a code written by someone else

# al the py modules -> google it

import math
import calendar

# import from same directoty
import module2

# import from sub directoty
import module_folder.module1 as module1

# import from other directory other than current directory or sub-directoty
import sys
# sys.path.append("E:\codebasics-ml\module_outside")
# import module3 # is not working

print(dir(math)) # all the function available in the module or we can google it

print(math.pow(2,5))
print(math.sqrt(16))
print(math.log10(1000))
print(round(math.pi,2))
print(math.floor(3.6))
print(math.ceil(3.6))


print(dir(calendar))
print(calendar.month(2022,11))
print(calendar.isleap(2022))
print(calendar.isleap(2016))

# dir
print(module2.area_of_square(4))

# sub-dir
print(module1.area_of_triangle(3,6))

# dir other that current of sub
# print(module3.add(2,3))