"""
    @authors Wes Oakley, Cameron Oakley
    @date 2023-10-11
    @details
"""

""" LIBRARIES """
import discord # used to integrate with discord bot api
import json # used to serialize api data
from keep_alive import keep_alive
import logging
import os
import requests # used for api requests

""" GLOBAL VARIABLES """
my_secret = os.environ['TOKEN']
intents = discord.Intents.default()  # Create instance of class Intents
intents.message_content = True  # Enable message_content intent
client = discord.Client(intents=intents)  # Pass intents to Client


""" FUNCTIONS """
def encodeData(str) : 
    # remove special chars with encoded letters
    
def fetchData(str) :
    # fetch data from youtube
    res = requests.get("https://www.youtube.com/results?search_query=")
    
def get_Quote() :
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    
    return(quote)

""" CLIENT EVENTS """
@client.event
async def on_ready() :
    print('We have logged in as {0.user}'.format(client))

""" START OF ON_MESSAGE """
@client.event
async def on_message(message) :
    #print(f'Message received from: {message.author}') # Debug making sure function works
    #print(f'Content: {message.content}') # Debug making sure content is readable
    if message.author == client.user :
        return

    # Hello Command
    if message.content.startswith('$hello') :
        
        await message.channel.send('Hello!')
    
    # Inspire Command
    elif message.content.startswith('$inspire'):
        quote = get_Quote()
        
        await message.channel.send(quote)
    
    # handle youtube url
    elif message.content.startswith("$play") :
        # slice message input for url
        url = message[4:]
        logging.info("$play " + url)
        
        # preprocess url
        url = encodeData()
        # fetch data
        response = fetchData(url)
        
    # handle youtube search
    elif message.content.startswith("$search") :
        # slice message input for keyword(s)
        keyword = message[6:]
        logging.info("$search " + keyword)
        
        # preprocess keyword
        keyword = encodeData(keyword)
        # fetch data
        response = fetchData(keyword)
        
""" END OF ON_MESSAGE """

""" NAME-MAIN """
if __name__ == "__main__" :
    logging.info("STARTING THE BOT...")
    keep_alive() # heartbeat the flask web server
    client.run(my_secret) # Do not type token in plain text here!
    logging.basicConfig(filename='AggerBot.log', filemode='w', level=logging.INFO)