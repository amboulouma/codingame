import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())  # the number of temperatures to 
tab1 = []
tab2 = []
j=0
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    tab1.append(int(i))
    tab2.append(abs(int(i)))
    j += 1 

if len(tab2) == 0:
    min = 0
else:
    min = tab1[tab2.index(min(tab2))]
    if tab1.count(-min) >= 1 and tab1.count(min) >=1:
        min = abs(min)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(min)