def outed(meet, boss):
    total = 0
    item_count = len(meet)
    for person, score in meet.items():
        if person == boss:
            total += score*2
        else:
            total += score
    
    avg = total/item_count
    
    if avg <= 5:
        return "Get Out Now!"
    else:
        return "Nice Work Champ!"

#I fully passed this test in codewars. Here's the url to my completed solutions:
#https://www.codewars.com/users/CodeBoi0395/completed_solutions
 
#These tests are all copied from code wars. If true is printed, then the test is passed

print(outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura') == "Get Out Now!")
print(outed({'tim':1, 'jim':3, 'randy':9, 'sandy':6, 'andy':7, 'katie':6, 'laura':9, 'saajid':9, 'alex':9, 'john':9, 'mr':8}, 'katie') == "Nice Work Champ!")
print(outed({'tim':2, 'jim':4, 'randy':0, 'sandy':5, 'andy':8, 'katie':6, 'laura':2, 'saajid':2, 'alex':3, 'john':2, 'mr':8}, 'john') == "Get Out Now!")