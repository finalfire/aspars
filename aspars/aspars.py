from lark import Lark, Transformer
import pkgutil

_GRAMMAR_FILE = 'resources/asp_grammar.lark'

class ASParsTransformer(Transformer):
    """Transformer for converting an answer set into a JSON object.
    
    It is only used by the ASPars class.
    """
    def answerset(self, predicates):
        return list(predicates)
    def predicate(self, childrens):
        if len(childrens) > 1:
            name, extension = childrens
            arity = len(extension)
            return {'pred': name, 'ext': extension, 'arity': len(extension)}
        else:
            return {'name': childrens[0]}
    def extension(self, params):
        return list(params)
    def param(self, token):
        if token[0].type == 'NUMBER':
            return int(token[0].value)
        return token[0].value
    def name(self, token):
        return token[0].value


class ASPars:
    def __init__(self):
        self.grammar = pkgutil.get_data(__name__, _GRAMMAR_FILE).decode('utf-8')
        self.parser = Lark(self.grammar, start='answerset', parser='lalr')
        self.transformer = ASParsTransformer()

    def parse(self, data):
        """Parse a single answer set or a list of.
        
        If `type(data) == str`, returns a singleton; otherwise, returns a generator."""
        if isinstance(data, str):
            return self._parse(data)

        return map(self._parse, data)

    def _parse(self, s):
        """Parse the representation of an answer set (e.g., a single row from the output of wasp, clasp, etc.).
        
        Returns an array of predicate contained in the answer set."""
        tree = self.parser.parse(s) 
        return self.transformer.transform(tree)
