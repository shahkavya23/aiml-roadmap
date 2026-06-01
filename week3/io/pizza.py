import csv 
import sys
from tabulate import tabulate


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2 : 
    sys.exit("Too many command-line arguments")


if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


try:
    with open(sys.argv[1]) as file:
        menu_list =  csv.reader(file)

        formatted_table = tabulate(menu_list,headers="firstrow" , tablefmt="grid")
    
        print(formatted_table)

except FileNotFoundError:
    sys.exit("File does not exist")








