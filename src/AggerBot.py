import discord
import os
import requests
import json
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']
intents = discord.Intents.default()  # Create instance of class Intents
intents.message_content = True  # Enable message_content intent
client = discord.Client(intents=intents)  # Pass intents to Client

def get_Quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #print(f'Message received from: {message.author}') # Debug making sure function works
    #print(f'Content: {message.content}') # Debug making sure content is readable
    if message.author == client.user:
        return

    # Hello Command
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    # Inspire Command
    if message.content.startswith('$inspire'):
        quote = get_Quote()
        await message.channel.send(quote)

keep_alive()
client.run(my_secret) # Do not type token in plain text here!
