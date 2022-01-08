#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
File: main.py
Authors:
  ADRIÁN FLEITAS DE LA ROSA <alu0101024363@ull.edu.es>
  THADDAUS HAASE <alu0101016733@ull.edu.es>
  FRANCISCO JESUS MENDES GOMEZ <alu0101163970@ull.edu.es>
  SERGIO TABARES HERNÁNDEZ <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program transforms a SAT problem into it's 3SAT version.
'''

import sys

from SAT import SAT
from SAT2SAT_3 import SAT2SAT_3


def run():
    '''Main function to execute the program.'''
    if len(sys.argv) != 3:
        sys.exit("python " + sys.argv[0] + \
                 " path_to_sat_prob.json path_to_3_sat_resul_prob.json")
    sat_filename, sat3_filename = sys.argv[1:]

    problem = SAT(sat_filename)
    print(problem)
    print("The SAT problem has been loaded.\n")

    result = SAT2SAT_3.transform(problem)
    print(result)
    print("The 3SAT problem has been generated.\n")

    result.to_json(sat3_filename)
    print(f"The {sat3_filename} has been exported.")


if __name__ == "__main__":
    run()
