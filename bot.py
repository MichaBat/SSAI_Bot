import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user}')
    try:
        bot.load_extension('cogs.setup')
        print('Cogs loaded successfully!')
    except Exception as e:
        print(f"Error loading cog: {e}")

if __name__ == '__main__':
    print('Starting bot...')
    bot.run(DISCORD_TOKEN)
