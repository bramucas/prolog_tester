# Prolog tester

Python package for testing prolog predicates.

The user specifies a set of queries and their expected results, and tests them against a particular implemetation that must be in a prolog source code file.

## Test format

Tests are modelled as a JSON file with the following fields.
  * `"test_name"`: Name for identifying the test.
  * `"query"`: Prolog query to be tested. Must use a predicate that exists in the source code file.
  * `"expected_result"`: A list of JSON objects with pairs `"VariableName"` and `Value` which represents the expected output that prolog should answer to the query.
  * `"test_type"`: Configures how the expected results must be compared against the actual results.
    * Type value `"match"`: Actual result must be identical to the Expected result. Disregarding its order.
    * Type value `"contains"`: Actual result must be contained in (but not necessarily be the same than) the Expected result. Disregarding its order.

#### Example
```json
{
    "test_name": "sublist [1,2,3]",
    "query": "sublist(S,[1,2,3])",
    "test_type": "match",
    "expected_result": [
        {"S": []},
        {"S": []},
        {"S": []},
        {"S": []},
        {"S": [1]},
        {"S": [1,2]},
        {"S": [1,2,3]},
        {"S": [2]},
        {"S": [2,3]},
        {"S": [3]}
    ]
}
```

## CLI usage
```bash
prolog_tester tests/ prolog_file.pl
```

## API usage
```python:api_example.py

```
