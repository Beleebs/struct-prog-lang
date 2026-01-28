import re
import sys
from pprint import pprint

# p = re.compile("ab*")

# if len(sys.argv) > 1:
#     if p.match(sys.argv[1]):
#         print("match")
#     else:
#         print("not match")

patterns = [
    (r"\s+", "whitespace"),
    (r"\d+", "number"),
    (r"\+", "+"),
    (r"\-", "-"),
    (r"\/", "/"),
    (r"\*", "*"),
    (r".", "error"),
]

# Comprehension
# goes like this:
# for every p, tag in patterns:
# take every element and compute re.compile(p) coupled with tag
# place the result of everything back into patterns
# faster than a for loop...
patterns = [(re.compile(p), tag) for p, tag in patterns]

# tokenize function
# takes in characters for parameter
def tokenize(chars):
    "Tokenize a string using the patterns above"
    tokens = []
    pos = 0
    line = 1
    column = 1
    current_tag = None

    while pos < len(chars):
        for pattern, tag in patterns:
            # partial match at pos
            match = pattern.match(chars, pos)
            if match:
                current_tag = tag
                break
        assert match is not None
        value = match.group(0)

        # if there is an unexpected character, throw an exception
        if current_tag == "error":
            raise Exception(f"Unexpected character: {value!r}")
        
        # otherwise, take in tokens until whitespace is hit
        if current_tag != "whitespace":
            token = {"tag": tag, "line": line, "column": column}
            # check to see if its a number, add that value to the 
            if current_tag == "number":
                token["value"] = int(value)
            tokens.append(token)

        # checks to see if the character is a new line or just new character
        # if new line, increment line and reset column
        # otherwise, increment column
        for ch in value:
            if ch == "\n":
                line += 1
                column = 1
            else:
                column += 1
        position = match.end()

        tokens.append({"tag": None, "line": line, "column": column})
        return tokens


def test_digits():
    print("testing tokenize digits")
    t = tokenize("123")
    assert t[0]["tag"] == "number"
    assert t[0]["value"] == 123
    assert t[1]["tag"] is None
    t = tokenize("1")
    assert t[0]["tag"] == "number"
    assert t[0]["value"] == 1
    assert t[1]["tag"] is None

def test_operators():
    print("testing operators")
    t = tokenize("+ - / *")
    tags = [tok["tag"] for tok in t[:-1]]
    assert tags == ["+", "-", "/", "*"]

if __name__ == "__main__":
    test_digits() 
    test_operators()
    print("done.")           

        