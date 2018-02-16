import threading
import time
import sys
import random
print ("Welcome to the Algebra Quiz: Python Edition!")
print ("Question 1.")
time.sleep(1.0)
#    t = Timer(10.0, answer) # sets up timer
x = random.randint(1, 30)
y = random.randint(1, 30)
a = random.randint(1, 30)
print ("Evaluate 4x+7y+2a*-3^2.")
print ("where x equals")
print (x)
print ("y equals")
print (y)
print ("and A equals")
print (a) 
#   t.start() # starts the timer
answer_answer = int(input("Answer: "))
correct_answer = answer
if answer_answer == -36:
    print ("Yay! Next question: Evaluate 22x*4y where x=10 and y=2.")
 
    
elif answer_answer == "":
    print ("No blanks!")
    
else:
    print ("Fail!")
    sys.exit()
