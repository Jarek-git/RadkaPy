import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables
load_dotenv()

# Set up bot prefix and description
bot = commands.Bot(command_prefix='!', description='A Discord bot')

# Load bot extensions
bot.load_extension('cogs.example')

# Define event handler for bot initialization
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')

# Define error handler for bot commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command, please try again.')

# Define main function to run the bot
def main():
    # Set up Discord bot token
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        print('DISCORD_TOKEN environment variable not found.')
        return

    # Run the bot
    bot.run(token)

if __name__ == '__main__':
    main()
