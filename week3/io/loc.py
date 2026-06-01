import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2 : 
    sys.exit("Too many command-line arguments")



if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")


try:
    with open(sys.argv[1] , "r") as file:
        file_lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")



count = 0



for line in file_lines:
    if line.strip() ==  "":
        continue
    if line.strip().startswith("#"):
        continue
    
    count = count + 1



print(count)

