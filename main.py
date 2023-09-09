def recur_factorial(n):
 if n == 1:
  return n
 else:
  return n * recur_factorial(n-1)
 
  
num = int(input("enter a number:")) 
if num < 0:
  print("Sorry, factorial does not exist for negative factorial") 
elif num == 0:
  print("the factorial of 0 as 1") 
else: 
  print("the factorial of",num, "is", recur_factorial (num)) 