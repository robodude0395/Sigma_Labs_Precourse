#This is my initial "messy solution" which completed all 3999 tasks in 11 ms
#The "Solution_Optimal" is the optimal solution I worked out after submission

#Link to leetcode solution:
#https://leetcode.com/problems/roman-to-integer/solutions/7232329/my-solution-by-omar_maaouane_veiga_0395-zwl5 

class Solution_Messy:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
        nums = [roman_to_int_dict[letter.upper()] for letter in list(s)]
        count = len(s) -1
        result = 0
        
        skip = False
        for i in range(0, count):
            if skip:
                skip = False
                continue
            if(nums[i] < nums[i+1]):
                result += nums[i+1] - nums[i]
                skip = True
            else:
                result += nums[i]
        
        if(count != 0):
            if nums[-1] <= nums[-2]:
                result += nums[-1]
        else:
            result = nums[0]
        
        return result

class Solution_Optimal:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
        result = 0
        previous_value = 0

        for i in reversed(s):
            value = roman_to_int_dict[i]

            if previous_value > value:
                result -= value
            else:
                result += value
            
            previous_value = value
        else:
            return result
        
        return result

solver_messy = Solution_Messy()
solver_optimal = Solution_Optimal()


#This code shows the first three test cases for the leetcode problem using both
#the "messy" initial approach and the optimal solution worked out later.
print("-----MESSY SOLVER-----")
print(solver_messy.romanToInt("III") == 3)
print(solver_messy.romanToInt("LVIII") == 58)
print(solver_messy.romanToInt("MCMXCIV") == 1994)
print()
print("-----OPTIMAL SOLVER-----")
print(solver_optimal.romanToInt("III") == 3)
print(solver_optimal.romanToInt("LVIII") == 58)
print(solver_optimal.romanToInt("MCMXCIV") == 1994)