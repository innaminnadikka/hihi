'''a=int(input("enter the value"))
b=int(input("enter the value"))
p=a*b
print(p) '''
'''i=1
while(i<=500):
    n=i
    s=0
    while(n!=0):
        d=n%10
        s=s+d**3
        n=n//10
    #print(s)
    if(s==i):
        print("armstrong",s)
    i=i+1'''
#wrong
'''n=int(input("enter the value"))
for i in range(2,n+1):
    if(n%i==0):
        break
if(n==i):
    print("prime")
else:
    print("not prime")'''
    
n=int(input("enter the value"))
i=2

while(n!=1):
    if(n%i==0):
        print(i)
        n=n//i
        continue
    i=i+1
'''n=int(input("enter value"))
if(n==1 or n==2):
        print("prime")

else:
    for i in range(2,n+1):
        if(n%i==0):
            break;
    if(n==i):
        print("prime")
    else:
        print("not prime")'''
print(45//3)
              
            



















  
