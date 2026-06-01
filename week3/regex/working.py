import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Search for the exact time structure
    match = re.search(r"^([0-9]+)(?::([0-9]+))? (AM|PM) to ([0-9]+)(?::([0-9]+))? (AM|PM)$", s)
    
    if match:
        # Extract Time 1
        hour1 = int(match.group(1))
        if match.group(2):
            minute1 = int(match.group(2))
        else:
            minute1 = 0
        period1 = match.group(3)

        # Extract Time 2
        hour2 = int(match.group(4))
        if match.group(5):
            minute2 = int(match.group(5))  # Typo fixed here!
        else:
            minute2 = 0
        period2 = match.group(6)

    else:
        # Fails if the regex doesn't match the required format
        raise ValueError
    
    # Validate that hours and minutes are within physical bounds
    if not (1 <= hour1 <= 12 and 0 <= minute1 <= 59 and 1 <= hour2 <= 12 and 0 <= minute2 <= 59):
        raise ValueError
    
    # Convert hour1 to 24-hour format
    if period1 == "AM":
        if hour1 == 12:
            hour1 = 0
    else: # It is PM
        if hour1 != 12:
            hour1 += 12

    # Convert hour2 to 24-hour format
    if period2 == "AM":
        if hour2 == 12:
            hour2 = 0
    else: # It is PM
        if hour2 != 12:
            hour2 += 12

    # Format the return string with padded leading zeros
    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"

if __name__ == "__main__":
    main()