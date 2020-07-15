"""
3) Write a program to determine how many of the numbers between 1 and 10000 contains the
digit 3

"""
numbers = []
for n in range(1 , 14):
   digit = str(3)
   values = str(n)
   check = values.count(digit)
   if check == 1:
     integrate = numbers.append(check)
result = len(numbers)
print(result)







