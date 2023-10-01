import smtplib

# create SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sender", "password")

# message to be sent
message = "message"

# number of emails to send
num_emails = 1

for i in range(num_emails):
    # sending the mail
    s.sendmail("sender", "target", message)

# terminating the session
s.quit()
