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
import psycopg2
from modules.database import Database

# Load .env file
load_dotenv()

TOKEN = os.getenv('TOKEN')

DBNAME = os.getenv('DB_NAME')
USER = os.getenv('DB_USER')
PASSWD = os.getenv('DB_PASSWD')

# Init bot
bot = interactions.Client(token=TOKEN, 
                    presence=interactions.ClientPresence(
                        activities=[
                            interactions.PresenceActivity(
                                name="./null", 
                                type=interactions.PresenceActivityType.LISTENING
                            )
                        ]
                    ),
                    intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT
                    )

# Load cogs
bot.load('cogs.register')
bot.load('cogs.tags')

# Connect to database
db = Database(
    host='localhost', 
    dbname=DBNAME, 
    user=USER,
    passwd=PASSWD
)

# Create tables for database (if not exist)
db.create_tables()

# On ready event
@bot.event()
async def on_ready():
    print('Ready')

@bot.event()
async def on_message_create(message):
    if "sus" in message.content.lower():
        await message.create_reaction("🤨")

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
