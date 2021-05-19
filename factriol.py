def compute_factorial(n):
   
   if(n<=1):
       return 1
   else:
        return n*compute_factorial(n-1)
       
   

   

num = int(input())

res=compute_factorial(num)
print(res)
