import re
import sys

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

def tokenize(chars):
    "Tokenize a string using the patterns above"
    tokens = []
    pos = 0
    line = 1
    column = 1

    while pos < len(chars):
        for pattern, tag in patterns:
            # partial match at pos
            match = pattern.match(chars, pos)
            if (match):
                break
        assert match is not None

        