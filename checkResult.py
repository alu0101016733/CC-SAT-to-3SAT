#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
File: checkResult.py
Authors:
  ADRIÁN FLEITAS DE LA ROSA <alu0101024363@ull.edu.es>
  THADDAUS HAASE <alu0101016733@ull.edu.es>
  FRANCISCO JESUS MENDES GOMEZ <alu0101163970@ull.edu.es>
  SERGIO TABARES HERNÁNDEZ <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program checks if SAT problem is contained in
transformed 3SAT problem.
'''

import json
import logging
import sys

logger = logging.getLogger(__name__)

def getValue(c, value):
    if len(c) == 2:
        return not value
    return value

def solveClause(clause, variableDict):
    splittedValue = clause[0].split('!')
    result = False
    for value in clause:
        splittedValue = value.split('!')
        result = result or getValue(splittedValue,
            variableDict[splittedValue[-1]])
    return result

def solve3SATClause(clause, variableDict, addedVariableDict):
    splittedValue = clause[0].split('!')
    result = False
    for value in clause:
        splittedValue = value.split('!')
        if splittedValue[-1] in variableDict:
            result = result or getValue(splittedValue,
                variableDict[splittedValue[-1]])
        else:
            result = result or getValue(splittedValue,
                addedVariableDict[splittedValue[-1]])
    return result

def addLogicOne(values, order):
    for i in range(0, len(values)):
        if values[order[-1-i]]:
            values[order[-1-i]] = False
        else:
            values[order[-1-i]] = True
            break

def checkIfAllTrue(values):
    result = True
    for key in values:
        result = result and values[key]
    return result

def setAllToFalse(values):
    for key in values:
        values[key] = False

def checkSatAndSat3Files(sat_path, sat_3_path):
    sat_json = None
    sat_3_json = None

    satisResult = []

    with open(sat_path, "r") as file:
        sat_json = json.load(file)
        # self.variables = data['U']
        # self.clauses = data['C']

    with open(sat_3_path, "r") as file:
        sat_3_json = json.load(file)

    valuesNotStartingWithT = {}
    addedValuesIn3SAT = {}

    for i in sat_json['U']:
        valuesNotStartingWithT[i] = False

    for i in sat_3_json['U']:
        if i not in valuesNotStartingWithT and (i[0] == 'T' or i[1] == 'T'):
            addedValuesIn3SAT[i] = False
        elif i not in valuesNotStartingWithT:
            logger.info("NOT THE SAME")
            return False

    oderOfValuesNotStartingWithT = list(valuesNotStartingWithT.keys())
    orderOfAddedValuesIn3SAT = list(addedValuesIn3SAT.keys())

    counter = 0
    stopWhile = False
    while not stopWhile:
        # check result for sat problem
        logger.debug('SAT: %s', valuesNotStartingWithT)
        logger.debug('Starting SAT test')
        resultForSat = True
        for value in sat_json['C']:
            solvedClause = solveClause(value, valuesNotStartingWithT)
            resultForSat = resultForSat and solvedClause
            logger.debug('Clause: %s, Result: %s', value, solvedClause)
        logger.debug('SAT Result: %s', resultForSat)

        # check if 3SAT has member with same result as sat
        resultForSat3 = not resultForSat
        exit3SatCheck = False
        setAllToFalse(addedValuesIn3SAT)
        logger.debug('Starting SAT3 test')
        while not exit3SatCheck:
            tmpResultForSat3 = True
            logger.debug('3SAT Tvalues: %s', addedValuesIn3SAT)
            for value in sat_3_json['C']:
                solvedClause = solve3SATClause(value, valuesNotStartingWithT,
                    addedValuesIn3SAT)
                tmpResultForSat3 = tmpResultForSat3 and solvedClause
                logger.debug('Clause: %s, Result: %s', value, solvedClause)
            logger.debug('SAT3 Result: %s', tmpResultForSat3)
            if tmpResultForSat3 == resultForSat:
                resultForSat3 = tmpResultForSat3
                logger.debug('SAT to SAT3 Possible!')
                break
            exit3SatCheck = checkIfAllTrue(addedValuesIn3SAT)
            addLogicOne(addedValuesIn3SAT, orderOfAddedValuesIn3SAT)

        logger.debug('Complete SAT3 Result: %s', resultForSat3)

        if resultForSat:
            problemSatidfactible = valuesNotStartingWithT.copy()
            problemSatidfactible.update(addedValuesIn3SAT)
            satisResult.append(problemSatidfactible)
            logger.info(problemSatidfactible)

        stopWhile = checkIfAllTrue(valuesNotStartingWithT)
        addLogicOne(valuesNotStartingWithT, oderOfValuesNotStartingWithT)

        logger.debug('%s\nFinished test: %s\n%s', 80*'=', counter, 80*'=')
        counter += 1

        if resultForSat != resultForSat3:
            logger.info("NOT THE SAME")
            return [False, False]
    logger.info("Conversion was succesful")
    return [True, satisResult]

def run():
    if len(sys.argv) != 3:
        sys.exit("python " + sys.argv[0] + \
                 " path_to_sat_prob.json path_to_3_sat_resul_prob.json")
    sat_filename, sat3_filename = sys.argv[1:]
    checkSatAndSat3Files(sat_filename, sat3_filename)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()
