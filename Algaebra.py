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
print ("Evaluate 4x+7y+2a*3^2.")
print ("where x equals")
print (x)
print ("y equals")
print (y)
print ("and A equals")
print (a) 
#   t.start() # starts the timer
answer_answer = int(input("Answer: "))
correct_01 = (4 * x)
correct_02 = (7 * y)
correct_03 = (2 * a)
correct_answer = (correct_01 + correct_02 + correct_03 * 3 ** 2)
def question2():
    print ("Yay! Next question: Evaluate 22x*4y ")
    x = random.randint(1, 30)
    y = random.randint(1, 30)
    print ("where x equals")
    print (x)
    print ("and y equals")
    print (y)
    correct_01 = (22 * x)
    correct_02 = (4 * y)
    correct_answer = (correct_01 * correct_02)
    answer_answer = int(input("Answer: "))
    if answer_answer == correct_answer:
        question3()

if answer_answer == correct_answer:
  question2()  
 
    
elif answer_answer == "":
    print ("No blanks!")
    
else:
    print ("Fail!")
    sys.exit()

    
