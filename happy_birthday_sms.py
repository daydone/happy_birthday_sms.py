#The purpose of this application is to automatically send happy birthday messages to contacts by pulling the information from my apple contacts

#Needs to Pull data from my calendar once a day 
#The data that is important is BirthDate PhoneNumber ContactsName 
#I wonder if pulling the contact data into a database may work better
#Things I need to know (How to pull data from calendar app/How to send SMS with my script/Whether I need to store the data for my contacts or if I can just write a check in my script pointed at the API?)

if BirthDate=CurrentDate
sms.PhoneNumber ("Happy Birthday "ContactsName"! I hope you have a wonderful day"")