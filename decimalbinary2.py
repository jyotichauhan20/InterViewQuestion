import math

num= int(input("enter the number="))
max_length = math.floor(math.log(num, 2)) + 1
# Round numbers down to the nearest integer


for i in range(1, num+1):
    decimal = str(i).rjust(max_length)
    # it will return width and length
    octa = str(oct(i))[2:].rjust(max_length)
    hexa= str(hex(i))[2:].upper().rjust(max_length)
    binary= bin(i)[2:].lstrip('0').rjust(max_length)
    # returns a copy of the string with leading characters

    print('{} {} {} {}'.format(decimal,octa,hexa,binary))

    