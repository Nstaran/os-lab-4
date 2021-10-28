m = int(input('enter m '))
n = int(input('enter n '))

for i in range(m):
    if i%2==0:
       print(' * ',end='\t')
    else:
        print(' # ',end='\t')
for j in range(n):
    if j%2==0:        
        print(' # ',end='\t')
    else:
        print(' * ',end='\t')
        
        print()
