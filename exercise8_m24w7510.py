input_num = 0
break_num =0
list_num=[]
while(break_num != 999):
    input_num=input("Enter a positive number:")
    list_num.append(int(input_num))
    break_num = int(input_num)
print('Largest number:',max(list_num))
print('Smallest number:',min(list_num))