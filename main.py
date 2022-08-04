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
from modules import database

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
                    ))
bot.load('cogs.cog')

# Connect to database
conn = database.connect(
    host='localhost', 
    dbname=DBNAME, 
    user=USER,
    passwd=PASSWD
)
cursor = conn.cursor()

# Create tables for database (if not exist)
database.create_tables(cursor=cursor, connection=conn)

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

wallet = interactions.TextInput(
    style=interactions.TextStyleType.SHORT,
    label="Type your cryptowallet below:",
    custom_id="wallet_responce",
    min_length=26,
    max_length=36,
)
insta = interactions.TextInput(
    style=interactions.TextStyleType.SHORT,
    label="Type your instagram username below:",
    custom_id="insta_responce",
    min_length=1,
    max_length=30,
)
tg = interactions.TextInput(
    style=interactions.TextStyleType.SHORT,
    label="Type your telegram username below:",
    custom_id="telegram_responce",
    min_length=5,
    max_length=32,
)
@bot.command(
    name='reg',
    description='reg',
    scope=986529390064189451,
)
async def my_cool_modal_command(ctx):
    modal = interactions.Modal(
        title="Application Form",
        custom_id="mod_app_form",
        components=[wallet, insta, tg],
    )

    await ctx.popup(modal)

@bot.modal("mod_app_form")
async def modal_response(ctx, wallet, insta, tg):
    await ctx.send(f"You wrote: {wallet, insta, tg}", ephemeral=True)

# Start bot
bot.start()
