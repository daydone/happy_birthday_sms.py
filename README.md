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
