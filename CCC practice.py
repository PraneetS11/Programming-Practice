from distutils.spawn import find_executable
from gettext import find
from itertools import count


row_1 = list(input())
row_2 = list(input())
row1=list(set(row_1))
row2=list(set(row_2))
a = sorted(row1)
b = sorted(row2)
for i in row2:
    if i == "*":
        continue
    elif i in row1:
        c = row_1.count(i)
        d = row_2.count(i)
        if c>=d:
                final = 1

        else:
            final = 0
            break
    else:
        final = 0
        break
if final == 1:
    print("A")
else:
    print("N")






