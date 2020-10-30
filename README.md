# ASPars

Quick and easy parsing of Answer Sets into python dictionaries.

## Specification

ASPars allows the user to parse answer sets represented by the wasp output format, e.g., `{a, b(x), c(0), ...}`.

An answer set is parsed into a list of _predicate_. A predicate is represented as a dictionary with the following keys:
* `name`: name of the predicate,
* `ext`: a list of the (heterogeneous) values of the predicate,
* `arity`: arity of the predicate (e.g., length of the extension).

If the predicate is an atom, then only the `name` key is defined.

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

ASPars can be used by importing it or as a standalone module.


### Importing ASPars in a python program
```python
from aspars import ASPars

answer_sets = [
    '{a, foo(x), bar(-1,1), fizz("42")}',
    '{b, foo(y), bar(-2,2)}',
    '{c, foo(z), fizz("24")}',
]

# parse only the first answer set, returns a singleton
single = ASPars().parse(answer_sets[0])
# parse all the answer sets, returns an iterable (map)
multi = ASPars().parse(answer_sets)
```

### Using ASPars as a standalone module
```bash
$ cat my_answer_sets | python -m aspars
```