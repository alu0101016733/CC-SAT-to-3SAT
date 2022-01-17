#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
File: SAT.py
Authors:
  ADRIÁN FLEITAS DE LA ROSA <alu0101024363@ull.edu.es>
  THADDAUS HAASE <alu0101016733@ull.edu.es>
  FRANCISCO JESUS MENDES GOMEZ <alu0101163970@ull.edu.es>
  SERGIO TABARES HERNÁNDEZ <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program declares a class to represent a SAT problem.
'''

import json


class SAT:
    '''Class to represent a SAT problem.'''

    def __init__(self, json_path):
        '''Constructor of the SAT class.
        Parameters
        ----------
        json_path : string
            Path to the file with the definition of the SAT problem.
        '''
        self.variables = []
        self.clauses = []

        with open(json_path, "r") as file:
            data = json.load(file)
            self.variables = data['U']
            self.clauses = data['C']

        if not self.check_integrity():
            raise ValueError('Error: Wrong representation of SAT problem')

    def check_integrity(self) -> bool:
        '''Function to check the correct representation of the SAT problem.'''
        return self.check_variables() and self.check_clauses()

    def check_variables(self) -> bool:
        '''Function to check the correct representation of the variables of the
         variables.'''
        return len(self.variables) == len(set(self.variables))

    def check_clauses(self) -> bool:
        '''Function to check the correct representation of the variables of the
         clauses.'''
        for clause in self.clauses:
            for variable in clause:
                if variable.split('!')[-1] not in self.variables:
                    return False

        return True

    def __iter__(self) -> list:
        '''Function to make this object iterable trough it's variables.'''
        for clause in self.clauses:
            yield clause

    def __str__(self) -> str:
        '''Function to transform this object into a readable string.'''
        return f'U: {{{", ".join(self.variables)}}}\n' +\
            f'C: {{[{"], [".join([", ".join(c) for c in self.clauses])}]}}'

    def to_json(self, name='SAT.json'):
        '''Function to export this object to a json file.'''
        with open(name, "w") as file:
            json.dump({"U": self.variables, "C": self.clauses}, file, indent=2)


def run():
    '''Main function to test the SAT class.'''
    objeto = SAT('examples/SAT.json')
    print(objeto)
    for clause in objeto:
        print(clause)
    objeto.to_json('examples/test.json')


if __name__ == '__main__':
    run()
