# Boolean_Functions
Print minterms and truthtables of Boolean_Functions

## Simple usage case:
Print the truth table of boolean function expressed in variables or minterms.
```python
import truth_tables
x=eval(f"lambda a,b,c: ~a and ~c or ~b and ~c and {m[7]}")
boolfunct(x,3)
```
It prints

0 | 0 | 0 | 	 1

0 | 0 | 1 | 	 0

0 | 1 | 0 | 	 1

0 | 1 | 1 | 	 0

1 | 0 | 0 | 	 1

1 | 0 | 1 | 	 0

1 | 1 | 0 | 	 0

1 | 1 | 1 | 	 1

## boolfunct(x,n)
x is a boolean function of n variables

n in int number of variables
