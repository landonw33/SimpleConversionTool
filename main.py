calculation_to_hours = 24
name_of_units = "hours"


# function to do conversion
def days_to_units(num_of_days):
    return f"{num_of_days} days is {num_of_days * calculation_to_hours} {name_of_units}"

# function to validate input
def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        # only do conversion only for positive ints
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        # Won't do conversion for 0 days
        elif user_input_number == 0:
            print(f"You enter 0 days, please enter a positive number")
        # only case left is negative
        else:
            print("you entered a negative, no conversion for you")
    # When an invalid number is entered
    except ValueError:
        print("your input is not a valid number. Don't ruin my program")


# variable must be define before while
user_input = ""
while user_input != "exit":
    # get user input
    user_input = input("Enter the number as a comma separated list:\n")
    list_of_days = user_input.split(", ")
    # (list_of_days)
    # print(set(list_of_days))

    # print(type(list_of_days))
    # print(type(set(list_of_days)))
    # for loop to accept multiple inputs in a list
    # using set function to make sure list has no duplicates
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()


