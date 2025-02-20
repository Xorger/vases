import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Vases
#
# Australian Informatics Olympiad 2019
#
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of flowers.
N = None
a = None
b = None
c = None

# Read the value of N.
N = int(input().strip())

# TODO: This is where you should compute your solution. Store the number of
# flowers that should go in the first, second and third jars in the variables
# a, b and c. If it is impossible to arrange the flowers according to the
# rules, set each of these variables to 0.

if (num_minus_3 := N-3) > 2:
    a = num_minus_3
    b = 2
    c = 1
else:
    a = b = c = 0

# Print the answer.
print(a, b, c)
