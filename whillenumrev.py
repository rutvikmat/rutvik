# WP to read a number and display individual digits of a given number
# for example if we give 532 it should display 235
num=int(input("Enter a number"))
temp=0
while(num>0):
    temp=num%10
    print(temp)
    num=num//10
