from flask import Flask
import random

cnctest = Flaks(__name__)

@cnctest.route('/')
del output():
    n = random.randint(1,5)
    sum = 0

    for i in range(n):
        print("this is number of :" + str(i))
        sum += i*2
    return "the sum is: " + str(sum))
        
if __name__ =='__main__':
    cnctest.run(debug=True, host='0.0.0.0')
