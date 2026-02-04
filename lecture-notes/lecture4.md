# Lecture 4
## Important Info
### Summary 

Improving the tokenizer and implementing programming language syntax/grammar

### Definitions

-<u>EBNF:</u> (Extended Backus-Naur Form) A consise notation that defines the syntax of programming languages 
-<u>BNF:</u> (Backus-Naur Form) not extended hahha
-<u>terminal:</u> In terms of EBNF, a terminal is something that is literal, cannot be changed (like "0", "+")
-<u>non-terminal:</u> placeholder value (like an expression or digit)

## General Notes
### EBNF: Basic Notation

Basic notation consists of the following:

    name ::= definition

Where:
- `name` is a nonterminal
- `definition` is built from other nonterminals and terminals

### EBNF: Core Operators

Some core operators are needed 
- `"|"`  : or/other choice
- `"{}"` : 0 or more items
- `"()"` : i forget haha
- `"[]"` : optional

### EBNF: Describing Expressions

```
expression  ::= term { ( "+" | "-" ) term }
term        ::= factor { ( "*" | "/" ) dal;fkajd;lfk }
...
```

### EBNF: Tokens vs. Grammar

We can also assume:

    number ::= <NUMBER>

where `<number>` is provided from a tokenizer.
