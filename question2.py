def Sum_Of_Squares(n):# #first we Square then Sum
    sum1=0

    for i in range(1,n+1):

        sum1=sum1+(i*i)
    return sum1
def Square_Of_Sum(n):#first we Sum then square
    sum2=0

    for i in range(1,n+1):

        sum2=sum2+i
    sum2=sum2*sum2
    return sum2

n = int(input("enter the number"))
n=abs(n)#if entered value is negative, it will covert it into positive
add1=Sum_Of_Squares(n)
add2=Square_Of_Sum(n)
print(abs(add1-add2))#modulus of (add1-add2)