import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3 : 
    sys.exit("Too many command-line arguments")

cleaned_data = []


try:
    with open(sys.argv[1] , "r") as file:
        harry_dict = csv.DictReader(file)
        for row in harry_dict:
            last_name,first_name = row["name"].split(", ")
            cleaned_data.append({
                "first" : first_name,
                "last" : last_name,
                "house" : row["house"]
            })

        
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")



with open(sys.argv[2] , "w") as file:
        file_edit = csv.DictWriter(file , fieldnames = ["first" , "last" , "house"] )
        file_edit.writeheader()
        file_edit.writerows(cleaned_data)
        