from parser import parse

# recursive evaluation (bfs)
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
        return evaluate(ast["left"]) % evaluate(ast["right"])
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


if __name__ == "__main__":
    test_evaluate()
    print("testing complete")
