def FibRecursion(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibRecursion(n-1) + FibRecursion(n-2))  
num = int(input("Enter the number "))  
if num <= 0: 
   print("Please enter a positive integer")  
else:  
   print("Fibonacci series:")  
   for i in range(num):  
       print(FibRecursion(i))
