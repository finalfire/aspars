# ASPars

Quick and easy parsing of Answer Sets into python dictionaries.

## Compatibility

* wasp 

## Usage

```python
from aspars import ASPars

d = ASPars().parse('{a, foo(x), bar(-1,1), fizz("42")}')

# d is the following singleton:
# d = [
#   {'name': 'a'},
#   {'pred': 'foo', 'ext': ['x'], 'arity': 1}, {'pred': 'bar', 'ext': [-1,1], 'arity': 2}, {'pred': 'fizz', 'ext': ['"42"'], 'arity': 1}]
```