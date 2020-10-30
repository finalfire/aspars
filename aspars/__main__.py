from .aspars import ASPars
import json
import sys

def main():
    """Reads a line from `stdin` and parses it. Raises an exception if the line does not represent an answer set."""
    asparser = ASPars()
    for line in map(lambda row: row.rstrip(), sys.stdin):
        print(json.dumps(asparser.parse(line)))

if __name__ == "__main__":
    main()