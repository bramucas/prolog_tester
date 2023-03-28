# API usage example
from prolog_tester import PrologTestClass

ptc = PrologTestClass()
ptc.add_from_file('examples/sublist_1.json')
ptc.run_all_tests('examples/sublist.pl', verbose=True)

print(ptc.get_results())
