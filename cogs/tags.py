import interactions
from interactions.ext.files import command_send

class Tags(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client

    @interactions.extension_command(
        name='tag',
        description='Show useful tags',
        scope=986529390064189451,
    )
    async def tag(self, ctx):
        pass

    @tag.group()
    async def reg(self, ctx):
        pass

    @reg.subcommand(
        description="How to find Telegram UID?"
    )
    async def telegram(self, ctx):
        try:
            file = interactions.File(filename="./video_examples/telegram_uid.gif")
            await command_send(ctx, "Here is how you can find your Telegram ID:\n**1)** Open Telegram\n**2)** Search for `userinfobot`\n**3)** Press start, and copy your id\n\nVideo example:", files=file)
        except FileNotFoundError:
            await ctx.send("ERROR - Failed to locate video file...")
    
    @reg.subcommand(
        description="How to find Instagram username?"
    )
    async def instagram(self, ctx):
        try:
            file = interactions.File(filename="./video_examples/instagram_username.mov")
            await command_send(ctx, "Here is how you can find your Instagram username:\n**1)** Open Instagram\n**2)** Click on your profile picture\n**3)** Here you cand find your username\n\nVideo example:", files=file)
        except FileNotFoundError:
            await ctx.send("ERROR - Failed to locate video file...")
    
    @reg.subcommand(
        description="How to find MetaMask wallet address?"
    )
    async def wallet(self, ctx):
        try:
            file = interactions.File(filename="./video_examples/wallet_address.mov")
            await command_send(ctx, "\nVideo example:", files=file)
        except FileNotFoundError:
            await ctx.send("ERROR - Failed to locate video file...")

def setup(client):
    Tags(client)