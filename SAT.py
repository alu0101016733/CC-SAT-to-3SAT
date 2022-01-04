#Imports

import json
#Defición de la clase SAT

class SAT:
  def __init__(self, json_path):
    # Inicializacion 
    self.variables = []
    self.clauses = []
    with open(json_path, "r") as file:
      data = json.load(file)
      self.variables = data['U']
      self.clauses = data['C']
    
    if not self.check_integrity():
        raise ValueError('Error: Wrong representation of SAT problem')

  def check_integrity(self) -> bool:
    return self.check_variables() and self.check_clauses()
    
  def check_variables(self) -> bool: 
    return len(self.variables) == len(set(self.variables))

  def check_clauses(self)-> bool:
    for clause in self.clauses:
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

  def to_json(self, name = 'SAT.json'):
    with open(name, "w") as file:
      json.dump({"U": self.variables, "C": self.clauses}, file)


  

def run():
  objeto = SAT('SAT.json')
  print (objeto)
  for clause in objeto:
    print (clause)
  objeto.to_json('test.json')
  

if __name__ == '__main__':
  run()
  
