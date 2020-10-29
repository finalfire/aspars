from .aspars import ASPars
import json
import sys

if __name__ == "__main__":
    as_parser = ASPars()
    lines = map(lambda row: row.rstrip(), sys.stdin)
    answer_sets = as_parser.parse(lines)
    print(json.dumps(list(answer_sets)))