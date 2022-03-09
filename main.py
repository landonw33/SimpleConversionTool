# creating a function
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days is {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days is {num_of_days * 24 * 60} minutes"
    else:
        return f"unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print(f"You enter 0 days, please enter a positive number")
        else:
            print("you entered a negative, no conversion for you")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Enter the number of days and conversion unit:\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute()



"""
# example how access element of list
my_list = ["20", "30"]
print(my_list[1])
# ... of dict
my_dictionary = {"days": 20, "unit": "hours"}
print(my_dictionary["unit"])"""
