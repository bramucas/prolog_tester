from os.path import isdir
from os import listdir

import argparse

from ._prolog_test import PrologTestClass

def dir_path(string):
    if isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=dir_path)
parser.add_argument('filename', type=str)
args = parser.parse_args()


student_path = 'entregas/David Vaamonde Estévez_1985331_assignsubmission_file_'

ptc = PrologTestClass()
ptc.add_from_file('tests/sublist1_json')

ptc.run_all_tests(f'{student_path}/practica1.pl')

print(ptc.get_results())