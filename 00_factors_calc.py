# Functions go here

# Puts series of symbolys at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement 
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# displays intructions / infromation
def instructions(): 

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a integer that is more than (or equal to) 0")
    print()
    print("This program helps you find the factors for each number you enter.")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return""

# checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter an integer that is more than (or equal to)  {}".format(low) 

        try:

            # ask user to enter a number
            response = int(input(question))

            # check number more than zero and is less than 200
            if response >= 1:
                return response

            # outputs error if input is iinvalid
            else:          
                print(error)
                print()

        except ValueError:
            print(error)

# Get factors, return a sorted list
def get_factors(to_factor):
    
    # x**(0.5) is the square root of x
    # We want to loop untill we get to the square root of to_factor
    stop = int(to_factor**(0.5))
    
    factor_list = []

    for item in range(1, stop + 1):
        
        # if modulo is zero, then the number is a factor
        if to_factor % item == 0:
            
            # find second factor by dividing "to factor" by the fist factor
            factor_2 = int(to_factor / item)
            
            # Add first factors to list
            factor_list.append(item)
            
            # check second factor is in list and add it
            if factor_2 not in factor_list:
                factor_list.append(factor_2)
                
    # output
    factor_list.sort()
    return(factor_list)

# Main Routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow muitple calculations per session
Keep_going = ""
while Keep_going =="":

    comment = ""

    # ask user for number to be factored...
    print()
    var_to_factor = num_check("Number? ", 0)

    if var_to_factor !=1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "one is UNITY!   IT=t only has one factor. Itself :) "

    # comments for squraes / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 5 - 2:
        comment = "{} is a perfect square".format(var_to_factor) 

    # output factors and comment 
    if var_to_factor == 1:
        heading = "One is special.."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    Keep_going = input("Press <enter> to continue or any key to quit")
    print()

print()
print("-----Thank you for using the factor calculator-----")
print()