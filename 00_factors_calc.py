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
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit coulor (ie:24 per pixel). For text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
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

            # check number more than zero
            if response >= 1:
                return response

            # outputs error if input is iinvalid
            else:          
                print(error)
                print()

        except ValueError:
            print(error)

# Get factors, return a sorted list
def get_factors(get_factors):
    
    print()
    
 





     

# Main Routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow muitple calculations per session
Keep_going = ""
while Keep_going == "":

    Comment = ""

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
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor) 

    # output factors and comment 

    # Generate heading...
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
    keep_going = input("Press <enter> to see the instructions or any key to continue")
    print()

print()
print("Thank you for using the factor calculator")