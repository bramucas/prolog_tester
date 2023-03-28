from swiplserver import PrologMQI
import json

class PrologTestClass():
    tests = set()
    _results = {}
    def add_predicate_test(self, predicate_test):
        self.tests.add(predicate_test)

    def add_from_file(self, filename):
        self.tests.add(PredicateTest.from_json_file(filename))

    def run_all_tests(self, source_file, verbose=False):
        self._results = {test.test_name: test.run(source_file, verbose) for test in self.tests}

    def get_results(self):
        return self._results

class PredicateTest():
    @staticmethod
    def from_json_file(filename):
        with open(filename, 'r') as json_file:
            return PredicateTest.from_json(json.load(json_file))

    @staticmethod
    def from_json(json):
        if json['test_type'] == 'contains':
            return ContainsTest(
                test_name = json['test_name'],
                query = json['query'],
                expected_result= json['expected_result']
            )
        elif json['test_type'] == 'match':
             return MatchTest(
                test_name = json['test_name'],
                query = json['query'],
                expected_result= json['expected_result']
            )
        

    def __init__(self, test_name, query, expected_result):
        self.test_name = test_name
        self.query = query
        self.expected_result = expected_result

    def run(self, source_file, verbose):
        with PrologMQI() as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query(f'consult("{source_file}")')
                result = prolog_thread.query(f'{self.query}')
                if verbose:
                    print(f'----- Source: {source_file} | Test: {self.test_name} -----')
                    print(f'Expected:\n{self.expected_result}')
                    print(f'Obtained:\n{result}')
            return self._check_result(result)

class ContainsTest(PredicateTest):
    def _check_result(self, result):
        for element in self.expected_result:
            if element not in result:
                return False
        return True
    
class MatchTest(PredicateTest):
    def _check_result(self, result):
        _expected_result, _result = self.expected_result.copy(), result.copy()
        while _expected_result and _result:
            element = _expected_result.pop()
            try:
                _result.remove(element)
            except ValueError:
                return False
        return not _expected_result and not _result  # Both must be empty
