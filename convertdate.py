#Write a program that will convert mm-dd-yyyy to dd-mm-yyyy
import re

date = "Today is 11-29-2022"

print("This regex formula replaces mm-dd-yyyy format with dd-mm-yyy format")
print(re.sub("([0-9]{2})-([0-9]{2})-([0-9]{4})",r'\2-\1-\3', date))

