import sys
import re

# sys.stdout = open('./input.txt', 'w')
file = open('./day-3/input.txt', 'r')

# Read all lines from the file into a list
sections = file.readlines()

# Join all lines into a single string
section = ''.join(sections)

def multiply(section):
    """
    This function takes a string `section` and calculates the sum of the products
    of the numbers in the 'mul(n,m)' instructions present in the string.

    Args:
    section (str): The string containing the 'mul(n,m)' instructions.

    Returns:
    int: The sum of the products of the numbers in the 'mul(n,m)' instructions.
    """
    # Define the regular expression pattern to find 'mul(n,m)'
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    # Initialize the variable to store the sum of the products
    ans = 0

    # Find all matches of the pattern in the section
    for match in pattern.findall(section):
        n, m = map(int, match) # Convert the matches to integers
        ans += n * m # Add the product of n and m to the ans variable

    # Return the sum of the products
    return ans

print("Part 1:", multiply(section))

# Part 2
enabled = True  # Variable to control whether we are in an enabled state

clean_section = [] # List to store the cleaned section without 'don't()'

i = 0

while i < len(section):
    if enabled:
         # Check if the current substring is "don't()"
        if section[i:i+7] == "don't()":
            enabled = False # Disable processing
            i += 7 # Move the index past "don't()"
        else:
            clean_section.append(section[i]) # Add the current character to clean_section
            i += 1 # Move to the next character
    else:
        # Check if the current substring is "do()"
        if section[i:i+4] == "do()":
            enabled = True # Enable processing
            i += 4 # Move the index past "do()"
        else:
            i += 1 # Skip the current character
            
# Join the cleaned characters into a single string
clean_section = "".join(clean_section)

print("Part 2:",multiply(clean_section))