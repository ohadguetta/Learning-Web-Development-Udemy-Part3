with open('emails.txt','r') as file:
    emails = file.readlines()

for email in emails:
    if 'hotmail' in email:
        print('Good:',email.rstrip())
        hotmail = email.rstrip()
