input_num = 0
p_sum = 0
p_count= 0
n_sum = 0
n_count = 0
while(input_num != 999):
  input_num = int(input("Enter a number : "));
  if input_num >= 0:
    p_sum +=input_num
    p_count +=1
  elif input_num < 0:
    n_sum +=input_num
    n_count +=1
print('Positive count: ', p_count-1, 'Positive sum:', p_sum-999);
print('Negative count: ', n_count, 'Negative sum:', n_sum);