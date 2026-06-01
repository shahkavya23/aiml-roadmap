import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Check if the string matches the 4-part number format
    match = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    
    if match:
        # Loop through all 4 groups dynamically
        for i in range(1, 5):
            group = match.group(i)
            # Check if it's between 0-255 AND has no leading zeros
            if not (0 <= int(group) <= 255 and str(int(group)) == group):
                return False
        return True
        
    return False

if __name__ == "__main__":
    main()