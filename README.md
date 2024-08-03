# Personal_Telegram_Bot

## Description
This project is a personalized Telegram bot that interacts with users by responding to their messages with pre-defined responses. The bot is designed to provide information about myself and to engage users in conversation.

## Features

- **Start Command**: Initiates a conversation with a welcome message.
- **Help Command**: Provides users with information on how the bot works.
- **Custom Command**: Responds with a predefined message for a custom command.
- **Message Handling**: Identifies whether the chat is in a group or private & Processes and responds to user messages based on predefined responses.
- **Error Logging**: Logs errors that occur during the bot's operation.

## Technologies

- **Python 3.10.5:**
  - The core programming language used to develop the bot.
    
- **Python telegram bot:**
  - A library that provides a wrapper for the Telegram Bot API to create Telegram bots.
 
## Prerequisites
- Python 3.x
- Virtualenv

## Installation

1. **Create a virtual environment:**
   ```sh
   pip install virtualenv
   virtualenv bot_env # 'bot_env' is just a name for the virtual environment, you can choose any name

2. **Activate the virtual environment:**
   
     **On Windows:**
   
       .\bot_env\Scripts\activate
   
     **On macOS/Linux:**
   
       source bot_env/bin/activate
       
3. **Install required packages:**
   
        pip install python telegram bot
        
## Creating Your Bot
1. **Create a bot using BotFather on Telegram:**

  - Start a conversation with BotFather.
  - Use the command /newbot to create a new bot.
  - Follow the prompts to set the name and username of your bot.
  - BotFather will provide an API token. Save this token for use in your code.
2. **Set bot details:**

  - Use the command /setdescription to set the bot's description.
  - Use the command /setabout to set the bot's about section.
  - Use the command /setuserpic to set the bot's profile picture.

## Usage
 1. **Obtain API Token from BotFather:**

  - After creating your bot, BotFather will provide an API token. Copy this token.
2. Set API Token and user_name in Code:

- In the code, replace 'TOKEN' with the API token you received from BotFather.
- In the code, replace 'BOT_USERNAME' with the user_name you setted.
  
3. Run the main.py File:
   python main.py

## Project Structure
main.py: The main script containing the code for the Telegram bot.
