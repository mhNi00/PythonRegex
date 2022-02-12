# Write a program that checks if a string contains only a certain set of characters (eg. a-z,A-Z and 0-9)
import re

login_good_1 = 'Examplelogin29'
login_good_2 = 'fantastic0LOGIN'
login_bad_1 = '#not_so_good'
login_bad_2 = 'b@dl0g!n'
print("This program returns True if string doesn't contain any special character")
print(login_good_1, ":", bool(re.search('(^[a-zA-Z0-9]*$)', login_good_1)))
print(login_good_2, ":", bool(re.search('(^[a-zA-Z0-9]*$)', login_good_2)))
print(login_bad_1, ":", bool(re.search('(^[a-zA-Z0-9]*$)', login_bad_1)))
print(login_bad_2, ":", bool(re.search('(^[a-zA-Z0-9]*$)', login_bad_2)))