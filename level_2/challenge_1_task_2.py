#I fully passed this test in codewars. Here's the url to my completed solutions:
#https://www.codewars.com/users/CodeBoi0395/completed_solutions

def digitize(n):
    n_str = map(int, str(n))
    return list(n_str)[::-1]

# Test cases
print(digitize(0) == [0])
print(digitize(7) == [7])
print(digitize(12345) == [5, 4, 3, 2, 1])
print(digitize(987654321) == [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(digitize(1002003) == [3, 0, 0, 2, 0, 0, 1])