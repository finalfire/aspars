# ASPars

Quick and easy parsing of Answer Sets into friendly python structures.

## Specification

ASPars allows the user to parse answer sets represented in the following formats:
* wasp format, e.g., `{a, b(x), c(y,...,z), ...}`,
* clasp format, e.g., `a b(x) c(y,...,z) ...`.

An answer set is parsed into a list of predicates. A predicate is represented as a dictionary with the following keys:
* `name`: name of the predicate,
* `ext`: a list of the (heterogeneous) values of the predicate,
* `arity`: arity of the predicate (e.g., length of the extension).

If the predicate is an atom, then only `name` is defined.

#### Example
`{a, foo(x), bar(42,"42")}` is parsed into the following singleton:
```python
[
    {'name': 'a'},
    {'name': 'foo', 'ext': ['x'], 'arity': 1},
    {'name': 'bar', 'ext': [42, '"42"'], 'arity': 2}
]
```

## Usage

ASPars can be used by simply importing it or as a standalone module.


### Importing ASPars in a python program
```python
from aspars import ASPars

answer_sets_waspf = [
    '{a, foo(x), bar(-1,1), fizz("42")}',
    '{b, foo(y), bar(-2,2)}',
    '{c, foo(z), fizz("24")}',
]

# parses only the first answer set, returns a singleton
single = ASPars(syntax='wasp').parse(answer_sets_waspf[0])
# parse all the answer sets, returns an iterable (map)
multi = ASPars(syntax='wasp').parse(answer_sets_waspf)

# example in clasp syntax
single = ASPars(syntax='clasp').parse('b foo(y) bar(-2,2)')
```

### Using ASPars as a standalone module
```bash
$ cat my_answer_sets | python -m aspars
```