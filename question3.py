N=0
while N<=0:
    try:
        N = int(input("which position of prime numbers u want"))
       
        raise ValueError("there is no prime in negative or zeroth position")
        
    except ValueError as err:
        if N<=0:
            print(err)
            
        
L=N
p=2
while N!=0:
    for i in range(2,p):
        if p%i==0:
            break
    else:

        if N==1:
            break
        N= N-1
    p=p+1
print("In the ",L,"position prime number is ",p)