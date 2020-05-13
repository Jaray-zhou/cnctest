import random



n = random.randint(1,5)
print(n)
sum = 0

for i in range(n):
    print("this is number of :" + str(i))
    sum += i*2

print("the sum is: " + str(sum))
