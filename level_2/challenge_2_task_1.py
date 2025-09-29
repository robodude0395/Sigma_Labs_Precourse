import random

num_range = (0,100)
correct_number = random.randint(num_range[0], num_range[1])

tries = 0

previous_guess = None

#I reused the "get_parameter" method from Level 1 challenge_3_task_2.py to ensure
#correct input can be obtained.
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

while True:
    guess_number = get_parameter(f"Enter number between {num_range}: ", int)
    
    if(guess_number > correct_number):
        print("Too high")
    elif(guess_number < correct_number):
        print("Too low")
    else:
        print("You Won!")
        break
    if(guess_number == previous_guess):
        tries += 1
    previous_guess = guess_number
    
print(f"You won after {tries} tries!")
    