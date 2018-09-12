# Twitch Chat Bot
A Twitch Chat bot written in python, that echos chat, reacts to chat !commands and console commands.

## Installation
 - Copy src to desired destination
 - Alter config.py file with connection configurations:
    - channel - Chat/stream name to connect
    - user - Twitch username
    - pwd - Twitch oauth token
 - Run by calling chatbot.py
 - To get a list of console command type help

## Adding chat commands
 - Write new command code as a new function in commands.py file;
 - Add to COMMANDS dictionary:
    - key: chat string to react, without "!"
    - value: new command pointer

## Future Work
 - Add message limiter to not infringe Twitch chat limit of <20 message in 30 seconds
