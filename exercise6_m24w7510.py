input_num = 0
p_count= 0
n_count = 0
while(input_num != -1):
  input_num = int(input("Enter a number : "));
  if input_num >= 0:
    p_count +=1
  elif input_num < 0:
    n_count +=1
print('Positive count: ', p_count);
print('Negative count: ', n_count);