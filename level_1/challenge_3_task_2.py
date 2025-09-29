import math #Allows ot use pre-written methods to obtain sums and products of lists

valid_operations = {"sum": sum, "product": math.prod} #Define which operations the user can perform
valid_multiples = [3, 5] #Define which mutiples we would want to include within our number list

#This method takes in a numbers list and applies the defined operation from valid_operations to "numbers"
#list parameter 
def compute_result(numbers, operation=None):
  if(operation == None):
    return None
  else:
    print(numbers)
    return valid_operations[operation](numbers)

#DEV NOTE: I renamed function from "ask_user_for_number" to "get_parameter".
#This was done in order to make the function's name more descriptive as it
#is also reused to get user parameters such as whether they want to exclude
#non multiples or specify which operation thet want to perform.
#This function keeps asking the user for input until the input is either the
#correct type or the input belongs within the "valid_input_list". 
#User will be prompted with the appropiate error depending on which condition
#is not met.
def get_parameter(prompt : str, expected_type : type, valid_input_list=None):
  while True:
    user_input = input(prompt)
    try:
      if(valid_input_list == None or user_input in valid_input_list):
        return expected_type(user_input) 
      else:
        raise LookupError

    except ValueError:
      print(f"Invalid input. Please enter a value of type {expected_type.__name__}.")

    except LookupError:
      print(f"Invalid input. Please enter a value within:\n{"\n".join(["  "+str(i) for i in valid_input_list])}\n")

#This method re-uses get_parameter method to ensure user inputs are meet the 
#desired requiements before computing anything. The method will ask for number
#limit of list, whether non_multiples are excluded and which operation the 
#user wants to apply.
#Afterwards, the sanitized inputs are returned as a tuple/
def ask_user_for_parameters():
  number = get_parameter("Enter number: ", int)
  exclude_non_multiples = get_parameter(f"Do you only want to compute multiples of {",".join([str(i) for i in valid_multiples])} [y/n]?", str, ["Y", "y", "N", "n"])
  operation = get_parameter(f"Enter operation type ({",".join(valid_operations.keys())}): ", str, list(valid_operations.keys()))

  return number, exclude_non_multiples, operation

#This method returns a list of sequential numbers until "limit".
#If the user selects to exclude non multiples (is_excluding_non_multiples=="y")
#the numbers are added if they are multiples of "multiples_to_include" integer list
def get_numbers_to_compute(limit, is_excluding_non_multiples, multiples_to_include):
  number_list = []

  if(is_excluding_non_multiples.lower() == "y"):
    for n in range(1, limit+1):
      for multiple in multiples_to_include:
        if(n%multiple == 0):
          number_list.append(n)
          break
  else:
    number_list =  [n for n in range(1, number + 1)]

  return number_list


#-----MAIN PROGRAM-----

#Get parameters the user specifies
number, exclude_non_multiples, operation = ask_user_for_parameters()

#Generate the list of number to compute
numbers_to_compute = get_numbers_to_compute(number, exclude_non_multiples, valid_multiples)

#Compute user result
computed_result = compute_result(numbers_to_compute, operation)

#Print result
print(f"Operation result is: {computed_result}")