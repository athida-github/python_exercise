reverse_num = 0
input_num = 0
while(input_num>=0):
  input_num = int(input("Enter number: "))
  if input_num > 0:
    reverse_num = int(str(input_num)[::-1])
    print("Reversed number:",reverse_num)
  elif input_num<0:
    print("Goodbye!​")