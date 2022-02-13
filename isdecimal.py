#Write a program that will check if a number has a precision of 2
import re

number = (21
 ,345.1
 ,9031.93
 ,10323.231
 ,1.31231
 ,1
 ,0
 ,-123.43
 ,-13.214 )
print("This program returns true if the number's decimal point has a precision of up to 2.")
for i in range(len(number)):
    stringForTesting = str(number[i])
    print(stringForTesting, ":", bool(re.search('(^-?[0-9]*$)|(^-?[0-9]*\.[0-9]{1,2}$)', stringForTesting)))

