#! python3
# phoneAndEmail.py - Find phone numbers and email adresses

import pyperclip, re

#Get the text off the clipboard
text = str(pyperclip.paste())

#Create regex for phone numbers
phoneNumberRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? #area code
    (\s|-|\.)?         #separator
    (\d{3})            #first three digits
    (\s|-|\.)          #separator
    (\d{4})            #last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)''', re.VERBOSE)

#Create regex for email addresses
emailAddressRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #username
    @                   # @ symbol
    [a-zA-Z0-9.-]+   #domain name
    (\.[a-zA-Z]{2,4})      #dot-something
)''', re.VERBOSE)

#Find all the matches in the clipboard text
matches = []
for groups in phoneNumberRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)

for groups in emailAddressRegex.findall(text):
    matches.append(groups[0])

#Copy the results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')