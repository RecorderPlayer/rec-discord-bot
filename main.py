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

# Register user
@bot.command(
    name="register",
    description="Register",
    scope=986529390064189451,
    options=[
        interactions.Option(
            type=interactions.OptionType.STRING,
            name='wallet',
            description='Wallet address',
            required=True
        ),
        interactions.Option(
            type=interactions.OptionType.STRING,
            name='instagram',
            description='Instagram username',
            required=True
        ),
        interactions.Option(
            type=interactions.OptionType.INTEGER,
            name='telegram',
            description='Telegram UID',
            required=True
        )
    ]
)
async def reg(ctx: interactions.CommandContext, wallet: str, instagram: str, telegram: int):
    await ctx.send(f"{wallet}, {instagram}, {telegram}")

# Start bot
bot.start()
