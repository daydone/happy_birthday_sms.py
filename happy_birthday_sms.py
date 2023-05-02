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
    
# Checks for any events in the iCloud calendar with a "Birthday" keyword in the summary that match today's date,
# and sends a customizable SMS message to the user's specified contacts.
def check_birthdays():
    api = pyicloud.PyiCloudService(username, password)
    cal = api.calendar.events()
    today = datetime.today().strftime('%m%d')
    include_list = config['contacts'].get('include', [])
    exclude_list = config['contacts'].get('exclude', [])
    message_template = config['contacts'].get('message_template', 'Happy Birthday {name}!')
    for event in cal:
        summary = event.get('summary')
        start = event.get('startDate').strftime('%m%d')
        if start == today and 'Birthday' in summary:
            name = summary.split('\'s')[0].replace('Birthday ', '')
            phone = event.get('phone', '')
            if name in include_list or (not exclude_list) or (name not in exclude_list):
                message = message_template.format(name=name)
                send_sms(my_number, message)

# Main function
if __name__ == '__main__':
    check_birthdays()
