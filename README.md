  **NOTE: This is a personal project that is provided as-is, and may not be actively maintained. Use at your own discretion.**

## Preface
  This project is designed to help me learn DevOps principles, specifically how to use GitHub Actions, Docker, and Python.

## Happy Birthday SMS
  This application automatically sends Happy Birthday messages to your contacts by pulling information from your Apple Contacts and Calendar.

## Prerequisites
  - Docker installed on your system
  - A `config.json` file saved in your home directory (`~/config.json`)

**An example `config.json` file can be found in the `happy_birthday_sms.py` directory.**

## Deploying the Application
  To deploy the application, follow these steps:

    1. Pull the Docker image from the repository:
        docker pull daydone/happy-birthday-sms

    2.Run the Docker container, mounting your config.json file into the container:
        docker run -v ~/config.json:/app/config.json daydone/happy-birthday-sms

The container will run the application and send messages to your specified phone number(s) for any contacts with a birthday on the current day.

If you need to make any changes to the config.json file, you can modify the file on your local machine and restart the Docker container. The changes will be automatically picked up by the application.

Happy birthday messaging!


Debugging and Common Issues
Here are some common issues and FAQs that might help you resolve any problems you encounter while using Happy Birthday SMS.

My contacts are not being loaded
Make sure that the iCloud account information in your config.json file is correct. Also, make sure that you have an active internet connection and that you can access iCloud contacts from your device.

I am not receiving any messages
Make sure that the Twilio account information in your config.json file is correct. Also, make sure that you have an active internet connection and that your phone number is valid and able to receive SMS messages.

The application is not running
Make sure that Docker is installed on your system and that you have pulled the daydone/happy-birthday-sms image from the Docker repository. Also, make sure that your config.json file is saved in the correct location and has the correct structure.

How can I modify the message template?
You can modify the message template by changing the message_template value in the contacts section of your config.json file. You can use {name} as a placeholder for the contact's name.

Can I include or exclude more than one contact?
Yes, you can include or exclude multiple contacts by adding them to the include or exclude list in the contacts section of your config.json file.

Is this project ready for production use?
No, this project is a work in progress and is not ready for production use. Use it at your own discretion.
