"""
Given n as input. Print following pattern using For loop.
n = 3
#
## 
###
"""

n = 5
for i in range(1,n+1):
  for j in range(0, i):
    print("# ", end="")
  print("\r")