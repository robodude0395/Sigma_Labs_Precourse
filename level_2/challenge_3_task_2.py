jane_doe = {"Name":"Jane Doe", "Age":42, "Employed":True} # Example dictionary for one person
tom_smith = {"Name":"Tom Smith", "Age":18, "Employed":True} # Another person
mariam_coulter = {"Name":"Mariam Coulter", "Age":66, "Employed":False} # Another person
gregory_tims = {"Name":"Gregory Tims", "Age":8, "Employed":False} # Another person

people = [jane_doe, tom_smith, mariam_coulter, gregory_tims] # Store all people in a list

#I added apply_lowercase parameter. When True it applies lowercase to all valid inputs and user input to ensure
#an option can be selected despite different lowercase or uppercase.
def get_parameter(prompt : str, expected_type : type, valid_input_list=None, apply_lowercase = False):
  while True:
    user_input = input(prompt) # Ask the user for input
    if(apply_lowercase):
      user_input = user_input.lower() # Convert user input to lowercase
      valid_input_list = [i.lower() for i in valid_input_list] # Convert valid inputs to lowercase too
    try:
      if(valid_input_list == None or user_input in valid_input_list):
        return expected_type(user_input) # Return converted input if it's valid
      else:
        raise LookupError # Raise custom error if input not in valid list

    except ValueError:
      # Raised if conversion to expected_type fails (e.g. trying to convert "abc" to int)
      print(f"Invalid input. Please enter a value of type {expected_type.__name__}.")

    except LookupError:
      # Raised when input is not in the valid_input_list
      print(f"Invalid input. Please enter a value within:\n{"\n".join(["  "+str(i) for i in valid_input_list])}\n")

def print_people_dict(people):
  for person in people: # Loop through each person dictionary
    for k, v in person.items(): # Loop through keys and values
      if(k=="Employed" and type(v)==bool): # Format employment status
        if v:
          v = "Yes"
        else:
          v = "No"
      print(f"{k}:{v}") # Print key-value pair
    print() # Blank line between people


#-----MAIN PROGRAM-----
valid_operations = ["add", "remove", "quit"] # Allowed user operations

print_people_dict(people) # Print initial list of people
break_loop = False

while True:
    # Ask user which operation to perform
    operation = get_parameter(f"Enter which operation you'd like to perform {valid_operations}: ", str, valid_operations, True)
    
    match operation:
        case "add":
            # Gather info for new person
            name = get_parameter("Enter your name: ", str)
            age = get_parameter("Enter your age: ", int)
            employed = get_parameter("Are you employed (y/n)? ", str, ["yes", "no", "y", "n"], True)
            employed_bool = False
            
            if(employed == "yes" or employed == "y"): # Convert answer to boolean
                employed_bool = True
            
            # Add new person dictionary to people list
            people.append({"Name":name.title(), "Age":age, "Employed":employed_bool})
        case "remove":
            # Ask user who to remove, only first name allowed
            person_to_remove = get_parameter("Who do you want to remove?\n(Only type their first name) ", str, list([person["Name"].split()[0] for person in people]), True)
            # Find the dictionary of the person with that first name
            person_entry = next((p for p in people if p["Name"].split()[0].lower() == person_to_remove), None)
            people.remove(person_entry) # Remove matching person
        case "quit":
            break_loop = True # Exit loop
        
    if break_loop:
       break
    
    print_people_dict(people) # Print updated list of people