#wp to read a number and display individual digits sum
num=int(input("Enter a number"))
temp=0
sum=0
while(num>0):
    temp=num%10
    sum=sum+temp
    num=num//10
print(sum)