def sum_of_multiples(n, a, b):
    sum = 0
    lst=[]
    for i in range(2, n):
        # If a or b is equal to zero
        if a==0:
            a=n
        if b==0:
            b=n
        
        if (i % a == 0 or i % b == 0):# If i is a multiple of a or b
            lst.append(i)
        
            sum= sum+i
 
    return lst, sum
n,a,b=-1,-1,-1
while n<0:
    
        n=int(input("pls enter a no below which u want multiples & value should be whole no"))
while a<0:
        a=int(input("frst nmber which multiples required & value should be whole no"))
while b<0:
        b=int(input("scnd number which multiples required & value should be whole no"))

listt, add=sum_of_multiples(n, a, b)
print("list of multiples",listt)
print("sum of multiples is", add)