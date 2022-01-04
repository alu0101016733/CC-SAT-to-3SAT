#Imports

import json
#Defición de la clase SAT_3

class SAT_3:
  def __init__(self, json_path = None):
    # Inicializacion 
    self.variables = []
    self.clauses = []

    if json_path is not None:
      with open(json_path, "r") as file:
        data = json.load(file)
        self.variables = data['U']
        self.clauses = data['C']
      
      if not self.check_integrity():
          raise ValueError('Error: Wrong representation of SAT_3 problem')

  def check_integrity(self) -> bool:
    return self.check_variables() and self.check_clauses()
    
  def check_variables(self) -> bool: 
    return len(self.variables) == len(set(self.variables))

  def check_clauses(self, clauses = None) -> bool:
    if clauses is None:
      clauses = self.clauses  
    for clause in clauses:
      if len(clause) != 3:
        return False
      for variable in clause:       
        if variable.split('!')[-1] not in self.variables:
          return False
    
    return True

  def __str__(self)-> str:
    return f'U: {{{", ".join(self.variables)}}}\n' +\
      f'C: {{[{"], [".join([", ".join(c) for c in self.clauses])}]}}'

  def __iter__(self)-> list:
    for clause in self.clauses:
      yield clause
  
  def add_clause(self, clause):
    if self.check_clauses([clause]) and clause not in self.clauses:
      self.clauses.append(clause)

  def add_variable(self,variable):
    if variable not in self.variables:
      self.variables.append(variable)

  def to_json(self, name = '3SAT.json'):
    with open(name, "w") as file:
      json.dump({"U": self.variables, "C": self.clauses}, file)

def run():
  objeto = SAT_3('3SAT.json')
  print (objeto)
  for clause in objeto:
    print (clause)
  objeto.to_json('3test.json')

if __name__ == '__main__':
  run()
  
