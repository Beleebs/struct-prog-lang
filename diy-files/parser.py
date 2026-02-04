# EBNF PARSER
# 
#   expression = term { ( "+" | "-" ) term }
from tokenizer import tokenize
from pprint import pprint

def parse_factor(tokens):
    """factor = <number>"""
    # ^^^ this is called a doc string
    token = tokens[0]
    # should be a number
    if token["tag"] == "number":
        node = {"tag":"number", "value":token["value"]}
        return node, tokens[1:]
    # if not, throw exception
    assert False, f"Expected number, got {token}"

def test_parse_factor():
    """factor = <number>"""
    print("test parse_factor()")
    tokens = tokenize("3")
    ast, tokens = parse_factor(tokens)
    assert ast == {'tag': 'number', 'value': 3}
    assert tokens == [{'column': 2, 'line': 1, 'tag': None}]
    print("complete")

# parses the term of the 
def parse_term(tokens): 
    """term = factor { ( "*" | "/" ) factor }"""
    left, tokens = parse_factor(tokens)
    while tokens[0]["tag"] in ["*", "/"]:
        op = tokens[0]["tag"]
        # [1:] is used to consume the token after finding op
        right, tokens = parse_factor(tokens[1:])
        left = {"tag": op, "left": left, "right": right}
    return left, tokens

def test_parse_term():
    """term = factor { ( "*" | "/" ) factor }"""
    print("test parse_term()", "3*4")
    tokens = tokenize("3*4")
    ast, tokens = parse_term(tokens)
    print("complete")
    exit()

if __name__ == "__main__":
    test_parse_factor()
    test_parse_term()
    print("testing complete")

