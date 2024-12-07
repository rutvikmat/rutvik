#WP to read a number and display individual digits of a given number
#for example if we give 532 it should display 235
def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number

i=(input("enter a number"))
rev = reverse_number(i)
print(rev)
