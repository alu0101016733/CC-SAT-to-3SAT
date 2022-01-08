#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
File: SAT_3.py
Authors:
  ADRIÁN FLEITAS DE LA ROSA <alu0101024363@ull.edu.es>
  THADDAUS HAASE <alu0101016733@ull.edu.es>
  FRANCISCO JESUS MENDES GOMEZ <alu0101163970@ull.edu.es>
  SERGIO TABARES HERNÁNDEZ <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program declares a class to represent a 3SAT problem.
'''

import json


class SAT_3:
    '''Class to represent a 3SAT problem.'''

    def __init__(self, json_path=None):
        self.variables = []
        self.clauses = []

        if json_path is not None:
            with open(json_path, "r") as file:
                data = json.load(file)
                self.variables = data['U']
                self.clauses = data['C']

            if not self.check_integrity():
                raise ValueError(
                    'Error: Wrong representation of SAT_3 problem')

    def check_integrity(self) -> bool:
        '''Function to check the correct representation of the 3SAT problem.'''
        return self.check_variables() and self.check_clauses()

    def check_variables(self) -> bool:
        '''Function to check the correct representation of the variables.'''
        return len(self.variables) == len(set(self.variables))

    def check_clauses(self, clauses=None) -> bool:
        '''Function to check the correct representation of the clauses.'''
        if clauses is None:
            clauses = self.clauses

        for clause in clauses:
            if len(clause) != 3:
                return False

            for variable in clause:
                if variable.split('!')[-1] not in self.variables:
                    return False

        return True

    def add_clause(self, clause):
        '''Function to add a clause into this 3SAT problem clauses.'''
        if self.check_clauses([clause]) and clause not in self.clauses:
            self.clauses.append(clause)

    def add_variable(self, variable):
        '''Function to add a variable into this 3SAT problem variables.'''
        if variable not in self.variables:
            self.variables.append(variable)

    def __iter__(self) -> list:
        '''Function to make this object iterable trough it's variables.'''
        for clause in self.clauses:
            yield clause

    def __str__(self) -> str:
        '''Function to transform this object into a readable string.'''
        return f'U: {{{", ".join(self.variables)}}}\n' +\
            f'C: {{[{"], [".join([", ".join(c) for c in self.clauses])}]}}'

    def to_json(self, name='3SAT.json'):
        '''Function to export this object to a json file.'''
        with open(name, "w") as file:
            json.dump({"U": self.variables, "C": self.clauses}, file)


def run():
    '''Function to test the 3SAT class.'''
    objeto = SAT_3('3SAT.json')
    print(objeto)
    for clause in objeto:
        print(clause)
    objeto.to_json('3test.json')


if __name__ == '__main__':
    run()
