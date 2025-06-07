## Name :Aye Thida
## StID :M24W7510
## Date :30 Nov 2024
#####################

import random
print("--------guess number------------")
#Random Num generate
guess_num = int(random.random()*100)
#print(guess_num)
print("--------------------------------")

#Accepting input num from End User
input_num = int(input("Input Your Guess Number : "))
rep=1;
while rep<10:
  #The Condition when user guesses the number correctly
  if(guess_num == input_num):
    print("Congratulation! You Win.");
    print("The Total Number of Guess :",rep);#745
    print("---------- End Game ------------");
    break
  
  #The Condition when user guesses the number smaller
  elif(guess_num > input_num):
    print("The number you entered is smaller! ", 10-rep,"chance remain.");
    input_num = int(input("Input Your Guess Number : "));
    rep=rep+1

  #The Condition when user guesses the number higher  
  elif(guess_num < input_num):
    print("The number you entered is higher! ", 10-rep,"chance remain.");
    input_num = int(input("Input Your Guess Number : "));
    rep=rep+1

#If the user guesses the number correctly
if(input_num==guess_num and rep==10):
 print("Congratulation! You Win.");
 print("The Total Number of Guess :",rep);
 print("---------- End Game ------------");

 #If the user guesses the number incorrectly
elif(input_num!=guess_num and rep==10):
 print("Sorry! You lost. The guess number is ", guess_num);
 print("The Total Number of Guess :",rep);
 print("---------- End Game ------------");
