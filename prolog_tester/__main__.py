from os.path import isdir
from os import listdir

import argparse

from ._prolog_test import PrologTestClass
from ._version import __version__

def version_text():
    return f'Version {__version__}'

def dir_path(string):
    if isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def _main():
    parser = argparse.ArgumentParser(
        prog='PrologTester',
        description='Tests prolog predicates.',
        epilog=version_text()
    )
    parser.add_argument('testfile', type=str, 
        help='File path to the JSON test file.',
    )
    parser.add_argument('sourcefile', type=str,
        help='File path to the prolog source code file to be tested.',                    
    )
    args = parser.parse_args()

    ptc = PrologTestClass()
    ptc.add_from_file(args.testfile)
    ptc.run_all_tests(args.sourcefile)

    print(ptc.get_results())

if __name__ == '__main__':
    _main()