from parser import parse
import math

flooredMod = False

# recursive evaluation
def evaluate(ast):
    # exit case!
    if ast["tag"] == "number":
        return ast["value"]
    elif ast["tag"] == "+":
        return evaluate(ast["left"]) + evaluate(ast["right"])
    elif ast["tag"] == "-":
        return evaluate(ast["left"]) - evaluate(ast["right"])
    elif ast["tag"] == "*":
        return evaluate(ast["left"]) * evaluate(ast["right"])
    elif ast["tag"] == "/":
        return evaluate(ast["left"]) / evaluate(ast["right"])
    elif ast["tag"] == "%":
        if flooredMod:
            # floored remainder, meaning that the sign of the result follows the value on the right
            return evaluate(ast["left"]) % evaluate(ast["right"])
        else:
            # truncated remainder, which isn't used by the % operand in python
            return math.fmod(evaluate(ast["left"]), evaluate(ast["right"]))
    else:
        raise ValueError(f"Unknown AST node: {ast}")
    
# test it
def test_evaluate():
    print("test evaluate()")
    # evaluate single number expression
    ast = {"tag": "number", "value": 3}
    assert evaluate(ast) == 3

    # evaluate operator and operand
    ast = {
        "tag": "+",
        "left": {"tag": "number", "value": 3},
        "right": {"tag": "number", "value": 6}
    }
    assert evaluate(ast) == 9

    # evaluate multi-level ASTs
    ast = {
        "tag": "+",
        "left": {"tag": "number", "value": 6},
        "right": {
            "tag": "*", 
            "left": {
                "tag": "number", "value": 5
                },
            "right": {
                "tag": "number", "value": 2
                },
            }
    }
    assert evaluate(ast) == 16
    print("complete")

def test_modulo():
    print("testing modulo operators")

    # x mod 1, should always be 0
    print("x % 1")
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 5},
        "right": {"tag": "number", "value": 1}
    }
    assert evaluate(ast) == 0

    # positive integers
    print("positive integers")
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 3},
        "right": {"tag": "number", "value": 2}
    }
    assert evaluate(ast) == 1

    # negative left value test, different between floored/truncated
    print("negative left")
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": -31},
        "right": {"tag": "number", "value": 2}
    }
    if flooredMod:
        assert evaluate(ast) == 1
    else:
        assert evaluate(ast) == -1

    # negative right value test
    # different between floored/truncated modulo
    print("negative right")
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 12},
        "right": {"tag": "number", "value": -5}
    }
    if flooredMod:
        assert evaluate(ast) == -3
    else:
        assert evaluate(ast) == 2

    # both negatives test
    print("both negative")
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": -30},
        "right": {"tag": "number", "value": -4}
    }
    assert evaluate(ast) == -2
    print("complete")

if __name__ == "__main__":
    if flooredMod:
        print("Floored Modulus")
    else:
        print("Truncated Modulus")
    test_modulo()
    print("testing complete")
