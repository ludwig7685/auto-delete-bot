import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Define the keywords to check for
keywords = ['https://discord.gg/', '.gg/', 'uwu', '', '', '', '']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if message contains any of the keywords
    if any(keyword in message.content for keyword in keywords):
        await message.delete()
        print(f'Deleted message from {message.author.name}: {message.content}')

    await bot.process_commands(message)

# Add more bot commands here if needed

# Start the bot
keep_alive()
bot.run('')
