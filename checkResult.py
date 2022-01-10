#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

sat_path = 'SAT.json'
sat_3_path = '3SAT.json'

sat_json = None
sat_3_json = None

with open(sat_path, "r") as file:
    sat_json = json.load(file)
    # self.variables = data['U']
    # self.clauses = data['C']

with open(sat_3_path, "r") as file:
    sat_3_json = json.load(file)

allVariables = {}

for i in sat_3_json['U']:
    allVariables[i] = False

for i in sat_json['U']:
    if i not in allVariables:
        print("NOT THE SAME")

orderedKeys = list(allVariables.keys())

def getValue(c, value):
    if len(c) == 2:
        return not value
    return value

def solveClause(clause, variableDict):
    splittedValue = clause[0].split('!')
    result = getValue(splittedValue, variableDict[splittedValue[-1]])
    for i in range(1,len(clause)):
        splittedValue = clause[i].split('!')
        result = result or getValue(splittedValue, variableDict[splittedValue[-1]])
    return result

stopWhile = False
while not stopWhile:
    stopWhile = allVariables[orderedKeys[0]]
    for i in range(1, len(orderedKeys)):
        stopWhile = stopWhile and allVariables[orderedKeys[i]]
        #print(allVariables[orderedKeys[i]], end=', ')
    # add 1 in binary to get next combination
    for i in range(0, len(allVariables)):
        if allVariables[orderedKeys[-1-i]]:
            allVariables[orderedKeys[-1-i]] = False
        else:
            allVariables[orderedKeys[-1-i]] = True
            break

    # check result for sat problem
    print('Checking: ', end='')
    print(allVariables)
    resultForSat = True
    print('SAT -> ', end='')
    for value in sat_json['C']:
        print(' ',value,'~',solveClause(value, allVariables), end=' --')
        resultForSat = resultForSat and solveClause(value, allVariables)
    print()
    # check result for sat 3 problem
    print('SAT3 -> ', end='')
    resultForSat3 = True
    for value in sat_3_json['C']:
        print(' ',value,'~',solveClause(value, allVariables), end=' --')
        resultForSat3 = resultForSat3 and solveClause(value, allVariables)
    print(end='\n\n')

    if resultForSat != resultForSat3:
        print("NOT THE SAME")
        break
