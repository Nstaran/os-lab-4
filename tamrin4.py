n=int(input("enter n :"))

def fibona(n): 
    if n==0: 
        return 0

    elif n==1: 
        return 1
    else: 
        return fibona(n-1)+fibona(n-2) 

x=[0]
for i in range(n):
 x.append(fibona(i+1))

print(x)