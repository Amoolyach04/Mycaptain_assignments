#fibonacci series 

def fib(n):  
   if n<=1:  
       return n  
   else:  
       return(fib(n-1)+fib(n-2))  
  
n_terms = int(input("Enter the number of terms:"))  
  
if n_terms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci series upto the given range: ")  
   for i in range(n_terms):  
       print(fib(i))