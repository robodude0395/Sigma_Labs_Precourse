# I put this method in a small script i can reference

# I added apply_lowercase parameter. When True it applies lowercase to all valid inputs and user input to ensure
# an option can be selected despite different lowercase or uppercase.
def get_parameter(prompt: str, expected_type: type, valid_input_list=None, apply_lowercase=False):
    while True:
        user_input = input(prompt)  # Ask the user for input
        if (apply_lowercase):
            user_input = user_input.lower()  # Convert user input to lowercase
            # Convert valid inputs to lowercase too
            valid_input_list = [i.lower() for i in valid_input_list]
        try:
            if (valid_input_list == None or user_input in valid_input_list):
                # Return converted input if it's valid
                return expected_type(user_input)
            else:
                raise LookupError  # Raise custom error if input not in valid list

        except ValueError:
            # Raised if conversion to expected_type fails (e.g. trying to convert "abc" to int)
            print(f"Invalid input. Please enter a value of type {expected_type.__name__}.")

        except LookupError:
            # Raised when input is not in the valid_input_list
            valid_values = '\n'.join(['  ' + str(i) for i in valid_input_list])
            print(f"Invalid input. Please enter a value within:\n{valid_values}\n")
