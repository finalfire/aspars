# ASPars

Quick and easy parsing of Answer Sets into python dictionaries.

## Compatibility

Currently, ASPars allows to parse answer sets represented by the wasp output format, e.g., `{a, b(x), c(0), ...}`.

## Usage

ASPars can be used importing it or as a standalone module.


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