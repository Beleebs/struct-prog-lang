# Lecture 3
## Important Info
### Summary 
- Techniques on how to interpret regular expressions.

### Definitions:
- <u>Entire String:</u> is the entire string the same as the other? (i.e. "truck" = "truck")
- <u>Partial String:</u> does the string contain the other string in some sort of capacity? (i.e. "truck" and "firetruck")
- <u>Character Set:</u> collection of characters mapped to unique numerical codes/IDs

## General Notes
### Character Sets
Things like:

    "\s" (space), "\d" (digit), "\n" (end line), "\t" (tab)

Can be used as <b>Character Sets</b>, to establish the difference between a string format and a number/tab/enter/etc.

Similarly, some specific characters can be used to modify how the regular expression is evaluated. For example, "+" and "*"

```
+ : 1 or more of previous character is allowed
* : 0 or more of previous character is allowed
```

Example:

    "be+n" can be "ben", "been", "beeeeeeeeeeeeen", but not "bn"
    On the contrary, "be*n" can use all of the above.

### OH BUT HOW DO WE DO OPERATORS IF THEY ARE SPECIAL CHARACTERS??!?!?!

We can use an escape infront of it.

    "\+", "\-", "\*", "\=", etc.

### Graphs

Just directed graphs on how to visualize the input strings.

### "car"

```
i want "car"

start:
if "c" = true:
    continue
else:
    fail

if "a" = true:
    continue
else:
    fail

if "r" = true:
    continue
else:
    fail

if anything 
    fail
else
    succeed
```

### "ca*r"

```
i want "ca*r"

start:
if "c" = true:
    continue
else:
    fail

node 1:
if "a" = true:
    continue node 2
else if "r":
    continue node 3
else:
    fail

node 2:
if "a" = true:
    continue node 2
else if "r" = true:
    continue node 3
else:
    fail

node 3:
if anything: 
    fail
else:
    continue succeed
```

### "ca+r"

```
i want "ca+r"

start:
if "c" = true:
    continue
else:
    fail

node 1:
if "a" = true:
    continue node 2
else:
    fail

node 2:
if "a" = true:
    continue node 2
else if "r" = true:
    continue node 3
else:
    fail

node 3:
if anything: 
    fail
else:
    continue succeed
```

or something of the sort.