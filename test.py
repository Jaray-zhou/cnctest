import random

n = random.randint(1,5)
sum = 0
for i in n:
  print("this is number of :" + i)
  sum += i*2
print("the sum is: " + sum)
