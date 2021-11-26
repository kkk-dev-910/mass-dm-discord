import sys, subprocess, json, time, asyncio
try:
    import discord, colorama, pyfade
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])
from discord.ext import commands
from colorama import Fore
from datetime import datetime
def error_msg():
    print("Error occured")

TOKEN = 'ODc3MTc5MTA0NDgxMzkwNjUz.YZlwOg.I-zwMitGPX2e9WcJTrM8AybAVaU'

def log_id(id, name, discriminator, guild):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(id, name, discriminator, guild)

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started logging IDs\n')

@bot.event
async def on_message(message):
    try:
        if not message.author.bot:
            try:
                reason = "MESSAGE"
                log_id(message.author.id, message.author.name, message.author.discriminator,
                        message.author.guild)
            except AttributeError:
                pass

        if message.author.bot:
            pass
    except AttributeError:
        pass
try:
    bot.run(TOKEN, bot=False)
except Exception as e:
    print(f"{Fore.RED}TOKEN ERROR - {e}")
    error_msg()
