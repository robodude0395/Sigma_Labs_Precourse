import random #Import python random library to generate random usernames
import string #Import string library to get character set

def reverse_name(name):
  """
  Returns a reversed string from input string "name"

  Parameters
  ----------
  name : str
    Any string (in this case a user's name)
  
  Returns
  -------
  str
    the reversed string of "name" parameter

  Examples
    --------
    >>> reverse_name("Omar")
    'ramO'
  """
  return name[::-1]


def intersperse_name(reversed_name, surname):
  """
  Returns the a string "reversed_name" insterspersed with the "surname" string
  This means evenly putting a character from reversed_name and surname one after
  other similar to merging two card decks

  Parameters
  ----------
  reversed_name : str
    This is the input string that is meant to be interlaced with the surname string
  
  surname : str
    This is the surname to be interlaced with the reversed_name string
  
  Returns
  -------
  str
    Interlaced result of reversed_name and surname

  Examples
    --------
    >>> reverse_name("amgis", "labs")
    'almagbiss'
  """

  split_reversed_name = list(reversed_name.strip())
  split_surname = list(surname.strip())

  result = ""
  smaller_word = []

  if(len(split_reversed_name) < len(split_surname)):
    smaller_word = split_reversed_name
    bigger_word = split_surname
  else:
    smaller_word = split_surname
    bigger_word = split_reversed_name
  
  for i in range(len(smaller_word)):
    result += split_reversed_name.pop(0) + split_surname.pop(0)
  result += "".join(bigger_word)
  
  return result

def format_name(name):
  """
  Formats input string "name" by splitting the name into two strings and returning
  the strings in capitalized format

  Parameters
  ----------
  name : str
    string (or name) to be split into a proper capitalized name and surname
  
  Returns
  -------
  tuple : (name, surname)
    name and surname are the split parts (by the midpoint) of the input string
    parameter

  Examples
    --------
    >>> format_name("almagbiss")
    ("Alma", "Gbiss")
  """

  midpoint = int(len(name)/2)
  return (capitalize(name[:midpoint]), capitalize(name[midpoint:]))

#For some reason .title() stops working properly when numbers are thrown into the mix
def capitalize(word):
  return word[0].upper() + word[1:].lower()

#Method to return a string of random characters 
#In this method I took the liberty of using string library character sets to
#save up time manually typing each entire character set.
def generate_random_string(lenght):
  return "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lenght))


# --------------------- MAIN PROGRAM ---------------------
print("Welcome to the username creator... Please choose one of the following options: ")
print("1.Create a username based on a name")
print("2.Generate a random username")

#Keep asking for a choice until a valid one is obtained
choice = input("Enter your choice here: ")
while len(choice) != 1 and choice.isdigit():
  print("Wrong input")
  choice = input("Enter your choice here: ")

#Generate a username from input name and surname
if(choice == "1"):
  #Create username from name and surname
  name = input("Enter your first name here: ")
  surname = input("Enter your surname here: ")

  reversed_name = reverse_name(name)
  interspersed_name = intersperse_name(reversed_name, surname)
  formatted_name, formatted_surname = format_name(interspersed_name)

  print(f"Your user name is {formatted_name} {formatted_surname}")

#Randomly generate a username
if(choice == "2"):
  random_name = generate_random_string(5)
  random_surname = generate_random_string(5)
  print(f"Your user name is {random_name} {random_surname}")