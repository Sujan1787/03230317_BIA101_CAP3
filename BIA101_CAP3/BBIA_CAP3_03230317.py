################################
# 
# sujan chhetri
# BBI A 
# 03230317
################################
# REFERENCES
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
# https://www.geeksforgeeks.org/python-extract-numbers-from-string/
################################
# SOLUTION
# Your Solution Score: <488662>
################################

# Solution Code

def read_input(file_name): # Reads the specified input file and returns a list of its lines.
    with open(file_name, 'r') as file: # Opens the specified file in read mode and assigns the file object to 'file'.
        lines = file.readlines() # Reads all lines from the file and stores them in a list.
    return lines # Returns the list of lines read from the file

def extract_two_digit_number(line):# Extracts a two-digit number formed by the first and last digits in the line.
    first_digit = None# Initializes the variable to store the first digit found in the line
    last_digit = None# Initializes the variable to store the last digit found in the line
    
    # Find the first digit from the start
    for char in line:# Iterates over each character in the line
        if char.isdigit(): # Checks if the character is a digit
            first_digit = char  # Assigns the first found digit to first_digit
            break# Exits the loop after finding the first digit
    
    # Find the last digit from the end
    for char in reversed(line):# Iterates over each character in the line in reverse order
        if char.isdigit(): # Checks if the character is a digit
            last_digit = char# Assigns the last found digit to last_digit
            break # Stops the loop iteration after finding the last digit
    
    if first_digit is not None and last_digit is not None:# Checks if both the first and last digits are found
        return int(first_digit + last_digit) # Forms a two-digit number from the first and last digits and returns it as an integer
    else:# Executes if either the first or last digit is not found
        return 0# Returns 0 when either the first or last digit is not found

def calculate_sum(file_name):    # Calculates the total sum of two-digit numbers extracted from each line in the input file.
    lines = read_input(file_name) # Reads the content of the input file into a list of lines
    total_sum = 0 # Initializes the total sum variable to zero
    
    for line in lines:# Iterates over each line in the list of lines
        number = extract_two_digit_number(line) # Extracts a two-digit number from the current line
        total_sum += number # Adds the extracted two-digit number to the total sum
    
    return total_sum# Returns the calculated total sum

def print_solution(file_name):# Prints the total sum of two-digit numbers extracted from the given input file.
    total_sum = calculate_sum(file_name) # Calculates the total sum of two-digit numbers from the input file
    print(f"The total sum of from the given input file {file_name} is {total_sum}")#This line of code prints the total sum of two-digit numbers extracted from a given input file, with placeholders for the filename (file_name) and the total sum (total_sum).

# Run the solution
#file_name = '317.txt'#assigns the filename '317.txt' to the variable file_name, which will be used to reference the input file during the program execution.
#print_solution(file_name)#It calls the function print_solution() with the argument file_name, which triggers the printing of the total sum of two-digit numbers extracted from the specified input file.








