#The purpose of this application is to automatically send happy birthday messages to contacts by pulling the information from my apple contacts

#Needs to Pull data from my calendar once a day 
#The data that is important is BirthDate PhoneNumber ContactsName 
#I wonder if pulling the contact data into a database may work better
#Things I need to know (How to pull data from calendar app/How to send SMS with my script/Whether I need to store the data for my contacts or if I can just write a check in my script pointed at the API?)

#if BirthDate=CurrentDate
#sms.PhoneNumber ("Happy Birthday "ContactsName"! I hope you have a wonderful day"")

import os
import sys
import json
import pyicloud
from icalendar import Calendar
from datetime import datetime
from twilio.rest import Client

# Read configuration from file
with open('~/config.json', 'r') as f:
    config = json.load(f)

# Twilio credentials
account_sid = config['twilio']['account_sid']
auth_token = config['twilio']['auth_token']
twilio_number = config['twilio']['twilio_number']
my_number = config['twilio']['my_number']

# iCloud credentials
username = config['icloud']['username']
password = config['icloud']['password']

# Function to send SMS alerts
def send_sms(number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=number,
        from_=twilio_number,
        body=message)
    print(f"Message sent to {number} with ID: {message.sid}")

# Function to check birthdays
def check_birthdays():
    api = pyicloud.PyiCloudService(username, password)
    cal = api.calendar.events()
    today = datetime.today().strftime('%m%d')
    for event in cal:
        summary = event.get('summary')
        start = event.get('startDate').strftime('%m%d')
        if start == today and 'Birthday' in summary:
            name = summary.split('\'s')[0].replace('Birthday ', '')
            phone = event.get('phone', '')
            send_sms(my_number, f"Happy Birthday, {name}!")
            
# Main function
if __name__ == '__main__':
    check_birthdays()
