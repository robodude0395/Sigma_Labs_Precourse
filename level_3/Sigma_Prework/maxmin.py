from math import inf

#More 'manual' method where each number is checked to determine the max num and the min num
#This method has O(n) time complexity
def min_max_linear(numbers):
    min_num = inf
    max_num = -inf

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    
    return [min_num, max_num]

#This method is better suited for larger lists since python's sorting method has O(nlogn) time complexity
#The method sorts the whole list and then returns the smallest (first number) number and the largest number (last number in sorted list)
def min_max_log(numbers):
    numbers.sort()
    return [numbers[0], numbers[-1]]

#----MAIN PROGRAM----

#These are a few tests to check the program works
print(min_max_linear([2,4,1,0,2,-1]))
print(min_max_log([2,4,1,0,2,-1]))
print()
print(min_max_linear([20,50,12,6,14,8]))
print(min_max_log([20,50,12,6,14,8]))
print()
print(min_max_linear([100,-100]))
print(min_max_log([100,-100]))