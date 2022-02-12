#Write a program that checks if input is a phone number
import re

phone_number_good_1 = "123456789"
phone_number_good_2 = "123 456 789"
phone_number_bad_1 = "34021523"
phone_number_bad_2 = "12345678p"

print("This program returns true if phone number contains 9 digits, it also accepts whitespace between every third digit")
print(bool(re.search('(^[0-9]{9}$|^[0-9]{3}\s[0-9]{3}\s[0-9]{3})', phone_number_good_1)))
print(bool(re.search('(^[0-9]{9}$|^[0-9]{3}\s[0-9]{3}\s[0-9]{3})', phone_number_good_2)))
print(bool(re.search('(^[0-9]{9}$|^[0-9]{3}\s[0-9]{3}\s[0-9]{3})', phone_number_bad_1)))
print(bool(re.search('(^[0-9]{9}$|^[0-9]{3}\s[0-9]{3}\s[0-9]{3})', phone_number_bad_2)))