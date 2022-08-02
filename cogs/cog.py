import interactions

class TestCommand(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client

    @interactions.extension_command(
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
    async def reg(self, ctx: interactions.CommandContext, wallet: str, instagram: str, telegram: int):
        await ctx.send(f"{wallet}, {instagram}, {telegram}")

def setup(client):
    TestCommand(client)