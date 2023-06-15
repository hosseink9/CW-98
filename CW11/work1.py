import sys
import os
from collections import Counter

num=len(sys.argv)
print("total arguments passed",num)

print('\n Name of python script: ', sys.argv[0])

print("\n arguments passed: ", end=" ")

if num == 1:
    print("Hello world")
else:

    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1],"r") as f:
            data=f.read()
            data=data.split()
            print(dict(Counter(data)),'\n')
    else:
        print(sys.argv[1][::-1],'\n')