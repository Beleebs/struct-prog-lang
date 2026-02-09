# Lecture 5
## Important Info
### Summary 

How to execute an AST, mini pieces that go into how it is evaluated

### Definitions

- <u>Evaluator:</u> Takes the operators/operands of an AST, performs actions upon them.

## General Notes
### Steps to Evaluating an AST

<b>THIS IS IMPORTANT!!!!!!!</b>

1. Identify Operators
2. Decide Operands
3. Evaluate Initial Operands
4. Execute the Operator and Evaluate Lazy Operands if present

### Recursive Calls

Recursive functions <b>NEED</b> 2 conditions:

1. Must have an exit condition
    - Ensures that algorithms can properly exit without wasting resources
2. Must recurse on a smaller problem set
    - Ensures that the algorithm can find the exit of recursion