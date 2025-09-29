def boredom(staff):
    department_scores = {"accounts":1,"finance":2,"canteen":10,"regulation":3,"trading":6,"change":6,"IS":8,"retail":5,"cleaning":4,"pissing about":25}
    total_score = 0
    
    for employee, department in staff.items():
        total_score += department_scores[department]
    
    outcome = "party time!!"
    
    if total_score > 80 and total_score < 100:
        outcome = "i can handle this"
    elif total_score <= 80:
        outcome = "kill me now"
        
    return outcome
  
#I fully passed this test in codewars. Here's the url to my completed solutions:
#https://www.codewars.com/users/CodeBoi0395/completed_solutions
 
#These tests are all copied from code wars. If true is printed, then the test is passed
print(boredom({"tim": "change", "jim": "accounts",
      "randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS",
      "laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts",
      "mr": "finance" }) == "kill me now")

print(boredom({ "tim": "IS", "jim": "finance",
      "randy": "pissing about", "sandy": "cleaning", "andy": "cleaning",
      "katie": "cleaning", "laura": "pissing about", "saajid": "regulation",
      "alex": "regulation", "john": "accounts", "mr": "canteen" }) == "i can handle this")

print(boredom({ "tim": "accounts", "jim": "accounts",
      "randy": "pissing about", "sandy": "finance", "andy": "change",
      "katie": "IS", "laura": "IS", "saajid": "canteen", "alex": "pissing about",
      "john": "retail", "mr": "pissing about" }) == "party time!!")