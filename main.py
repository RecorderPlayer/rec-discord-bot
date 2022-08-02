"""
RecorderPlayer Discord bot
In develop by ./null (Dmytro)
------------------------------
Interactions.py docs:
https://discord-interactions.readthedocs.io/en/latest/quickstart.html
"""

# Import necesary modules
import os
import interactions
from dotenv import load_dotenv

# Load .env file
load_dotenv()

TOKEN = os.getenv('TOKEN')

# Init bot
bot = interactions.Client(token=TOKEN, 
                    presence=interactions.ClientPresence(
                        activities=[
                            interactions.PresenceActivity(
                                name="to ./null", 
                                type=interactions.PresenceActivityType.LISTENING
                            )
                        ]
                    ))
bot.load('cogs.cog')

# On ready event
@bot.event()
async def on_ready():
    print('Ready')

# Just test command
@bot.command(
    name="test",
    description="Test Command",
    scope=986529390064189451,
)
async def test(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")

# Start bot
bot.start()
