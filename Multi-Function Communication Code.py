#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pywhatkit
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import vonage

input1 = input("Select an option (1 for WhatsApp, 2 for Email, 3 for SMS): ")

if input1 == "1":
    # WhatsApp message
    number = input("Enter the receiver's WhatsApp number (with country code): ")
    message = input("Enter the message: ")
    pywhatkit.sendwhatmsg_instantly(number, message)
    print("WhatsApp message sent successfully.")

elif input1 == "2":
    # Email
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'your_email@gmail.com'  # Replace with your Gmail email
    smtp_password = 'your_password'  # Replace with your Gmail password

    # Email content
    to_email = input("Enter the receiver's email address: ")
    subject = 'Test Email'
    message = input("Enter the email message: ")

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to Gmail's SMTP server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, to_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")

elif input1 == "3":
    # SMS using Vonage API
    client = vonage.Client(key="your_api_key", secret="your_api_secret")  # Replace with your Vonage API key and secret
    sms = vonage.Sms(client)

    to_number = input("Enter the receiver's phone number (with country code): ")
    sms_message = input("Enter the SMS message: ")

    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": to_number,
            "text": sms_message,
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("SMS sent successfully.")
    else:
        print(f"SMS failed with error: {responseData['messages'][0]['error-text']}")

else:
    print("Invalid input. Please select a valid option (1, 2, or 3).")


# In[ ]:





# In[ ]:




