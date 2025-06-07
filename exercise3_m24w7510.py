input_num = 0
sum = 0
count = 0
while(count != 5):
  input_num = int(input("Enter a number : "));
  sum += input_num
  count +=1
avg_num = sum/count
g_avgnum = int(input('Guess the average: '));
while(g_avgnum != g_avgnum):
  print('Wrong!')
  g_avgnum = int(input('Guess the average: '));
print('Correct!')