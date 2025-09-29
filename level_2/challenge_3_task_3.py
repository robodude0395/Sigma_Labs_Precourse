#I fully passed this test in codewars. Here's the url to my completed solutions:
#https://www.codewars.com/users/CodeBoi0395/completed_solutions

#This function takes in a list of ints and returns a list of single dictionary key:value pairs
#where the key represents the string number code of the character and the value represents the
#string value of the character.
def num_obj(s):
    #your code here
    return [{str(i): chr(i)} for i in s]