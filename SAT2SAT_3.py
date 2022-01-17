#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
File: SAT2SAT_3.py
Authors:
  ADRIÁN FLEITAS DE LA ROSA <alu0101024363@ull.edu.es>
  THADDAUS HAASE <alu0101016733@ull.edu.es>
  FRANCISCO JESUS MENDES GOMEZ <alu0101163970@ull.edu.es>
  SERGIO TABARES HERNÁNDEZ <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program declares a class with methods to transform a SAT
 problem into it's 3SAT version.
'''

from SAT import SAT
from SAT_3 import SAT_3


class SAT2SAT_3:
    '''Class to allocate the SAT to 3SAT problems transform methods.'''

    def __init__(self, problem_SAT=None):
        self.problem_SAT = problem_SAT
        self.problem_3SAT = SAT2SAT_3.transform(problem_SAT)

    @staticmethod
    def case1(clause, i=0):
        '''Function to transform the clauses with one variable.'''
        variables = [f"T{i}_0", f"T{i}_1"]
        clauses = [clause.copy(), clause.copy(), clause.copy(), clause.copy()]

        clauses[0].extend([variables[0],       variables[1]])
        clauses[1].extend([variables[0], '!' + variables[1]])
        clauses[2].extend(['!' + variables[0],       variables[1]])
        clauses[3].extend(['!' + variables[0], '!' + variables[1]])

        return variables, clauses

    @staticmethod
    def case2(clause, i=0):
        '''Function to transform the clauses with two variables.'''
        variables = f"T{i}_0"

        clauses = [clause.copy(), clause.copy()]
        clauses[0].append(variables)
        clauses[1].append(f"!{variables}")

        return [variables], clauses

    @staticmethod
    def case3(clause):
        '''Function to transform the clauses with three variables.'''
        return [], [clause]

    @staticmethod
    def case4plus(clause, i=0):
        '''Function to transform the clauses with four or more variables.'''
        variables = []
        for j in range(len(clause) - 3):
            variables.append(f"T{i}_{j}")

        clauses = []
        clauses.append([clause[0], clause[1], variables[0]])
        for j in range(1, len(variables)):
            clauses.append(
                ['!'+variables[j - 1], clause[j + 1], variables[j]])
        clauses.append(['!'+variables[-1], clause[-2], clause[-1]])
        return variables, clauses

    @staticmethod
    def transform(problem_SAT):
        '''Function to transform a given SAT problem into it's 3SAT version.'''
        problem_3SAT = SAT_3()
        problem_3SAT.variables = problem_SAT.variables.copy()
        new_variables = []
        new_clauses = []
        for i, clause in enumerate(problem_SAT):
            if len(clause) == 1:
                new_variables, new_clauses = SAT2SAT_3.case1(clause, i)
            elif len(clause) == 2:
                new_variables, new_clauses = SAT2SAT_3.case2(clause, i)
            elif len(clause) == 3:
                new_variables, new_clauses = SAT2SAT_3.case3(clause)
            elif len(clause) >= 4:
                new_variables, new_clauses = SAT2SAT_3.case4plus(clause, i)
            else:
                raise ValueError("Error: Invalid clause length")

            for new_variable in new_variables:
                problem_3SAT.add_variable(new_variable)
            for new_clause in new_clauses:
                problem_3SAT.add_clause(new_clause)

        return problem_3SAT


def run():
    '''Main function to test the SAT2SAT_3 class.'''
    problem = SAT('SAT.json')
    print(problem)
    objeto = SAT2SAT_3(problem)
    result = objeto.problem_3SAT
    print(result)


if __name__ == '__main__':
    run()
