#write program that checks if email is correct
import re
from pathlib import Path
textFile = Path('emails.txt').read_text()
textFile = textFile.replace('\n','')
matches = re.findall('([a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+)', textFile)
print("Here's a list of good emails!")
for x in matches:
    print(x)
print("Done1")
