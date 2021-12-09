# Python program to read
# json file
 
 
import json
 
# Opening JSON file
f = open('SAT.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

#print (data)
# Iterating through the json
# list
#for i in data['U']:
    #print(i)
 
# Closing file
f.close()

def case2(clause, i):
    variables = f"T{i}_0"
   
    clauses = [clause.copy(), clause.copy()]
    clauses[0].append(variables)
    clauses[1].append(f"!{variables}")

    return variables, clauses
    

a,b = case2(data['C'][0], 3)

print(a)
print(b)