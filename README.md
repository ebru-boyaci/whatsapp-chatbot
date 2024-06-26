
# WhatsApp-OpenAI Connection
Hi everyone, this is repository for my personal demo project on connecting Twilio and OpenAI to provide answers to all the users questions using OpenAI GPT-3. This is written in `Python` and served with `Flask`. This bot can only handle:
* text messgaes


### What you will need
There are couple of things that you need before you get started following this repository.
* OpenAI API key, since it is open to all, you can create an account [here](https://openai.com/) and access the key.
* You need a Twilio project, you can get `Account SID` and `Auth Token` for that project, we will need this to make requests. You can get it from [here](https://console.twilio.com/).
* API requesting application like Postman, Insomnia, etc.
* NGROK for local testing.

### How to use it
To replicate the work of this repository and run it locally, you need to follow these steps:
* create a `.env` file inside the root directory, create these environmental variables:
    ```
    TWILIO_ACCOUNT_SID=YOUR ACCOUNT SID
    TWILIO_AUTH_TOKEN=YOUR AUTH TOKEN
    OPENAI_API_KEY=YOUR OPENAI API KEY
    FROM=whatsapp:+14155238886
    ```
This FROM variable in the .env file is same for the Twilio WhatsApp Sandbox.

* create a virtual environment and activate it before installing the packages
python -m venv venv
source venv/bin/activate
* install all the required dependencies from the `requirements.txt` file
```python
pip install -r requirements.txt
```
* run the server with either of the following commands
```python
python run.py
```
```python
gunicorn run:app
```
* start NGROK engine on the same port as the python application is running.
* provide the NGROk urlon `Twilio WhatsApp Sandbox` for all incoming request.
* test the setup using your WhatsApp

This guide will walk you through the process of exposing your Flask application to the web using ngrok and setting this URL in the Twilio WhatsApp Sandbox for all incoming requests.

Step 1: Setting up and Starting Ngrok
* First, download and install ngrok from its official website.

* Before you run ngrok for the first time, you need to set up your authentication token. To get this, sign up and log in to the ngrok website. You can retrieve your auth token from the dashboard. Once you have your token, run the following command in your terminal:

```
./ngrok authtoken YOUR_AUTH_TOKEN
```
Replace YOUR_AUTH_TOKEN with the token you obtained.

* Start ngrok on the same port your application is running. On MacOS, Flask typically runs on port 5000, but for this example, we're using port 80. Start ngrok with the following command:
```
ngrok http 80
```
After this step, you should see a public URL generated by ngrok in your terminal. Copy this URL, as you will provide it to Twilio in the next step.

Step 2: Providing the Ngrok URL to Twilio WhatsApp Sandbox
* Log in to your Twilio account.
* Select Programmable Messaging from the left menu.
* Navigate to the WhatsApp tab.
* Go to the Sandbox section and paste the ngrok-generated URL into the WHEN A MESSAGE COMES IN field.

Step 3: Testing with WhatsApp
* Now that everything is set up, send a message from your personal WhatsApp number to the Sandbox and observe how your Flask application processes this message.# whatsapp-openai-chatbot

