# Reading and writing files in Python
"""
Keypoints : 
    1. Create a new file and write to it
    2. Reading file line by line
    3. File open modes
    4. With statements
"""
# f=open(file name and path, mode)

# write
f1=open("E:\\codebasics-ml\\python\\16_funny1.txt", "w") # it will overwrite
f1.write("I am Arunabha Mandal.")
f1.write(" I am Arunabha.")
f1.close()

# append
f2=open("E:\\codebasics-ml\\python\\16_funny2.txt", "a") # it will not overwrite insted it will append
f2.write("I am Kittu Mandal.\n")
f2.close()

# read , counting words
f3=open("E:\\codebasics-ml\\python\\16_funny3.txt", "r")
f_out=open("E:\\codebasics-ml\\python\\16_funny3_wc.txt", "w")
# print(f.read())
for line in f3:
    tokens=line.split(' ') # list of words in one line
    # print(str(tokens)) # won't show any number without str
    f_out.write("Wordcount:"+str(len(tokens))+" "+line)
    # print(len(tokens)) # word count

f3.close()
f_out.write("\n\nHi...")
f_out.close()


"""
r = Opens file for reading only. Throws error if file does not exist.
w = Opens file for writing only. If file does not exist then it will create new one. If it exits then it will overwrite it.
r+ = Opens file for both reading and writing.
w+ = Opens file for reading and writing. If file does not exist then it will create new one. If it exist then it will overwrite it.
a = Opens a file in append mode. Whatever you write to file will get appensed and original content will not be overwritten.
"""

# with statement
"""
You don't need to do f.close() if you use 'with'. Using 'with' will automatically close the file for you.
"""
with open("E:\\codebasics-ml\\python\\16_funny3.txt", "r") as f4:
    print(f4.read())

print(f4.closed)