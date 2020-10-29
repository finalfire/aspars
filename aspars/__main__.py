from .aspars import ASPars

if __name__ == "__main__":
    asp_parser = ASPars()
    x = asp_parser.parse('{a, b, foo(x), bar("ciao"), foobar(x, "ciao"), barfoo(10, "20", point)}')
    print(x, type(x))