number=int(input("Enter a number:> "))
n=0
while True:                           
    b=number
    while b==number:
        r=0
        n=n+1
        for x in range(1,n+1):
            if n%x==0:                  
                r=r+x
                if x==n:
                    if r==2*n:
                        print(n)
                        b=False
                    else:
                        b=False