import interactions
from cryptoaddress import EthereumAddress
import requests
from modules.database import Database
import os

DBNAME = os.getenv('DB_NAME')
USER = os.getenv('DB_USER')
PASSWD = os.getenv('DB_PASSWD')

class Register(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client
        self.db = Database(
            host='localhost', 
            dbname=DBNAME, 
            user=USER,
            passwd=PASSWD
        )

    @interactions.extension_command(
        name='register',
        description='Registration',
        scope=986529390064189451,
    )
    async def register_user(self, ctx):
        wallet = interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="Type your MetaMask cryptowallet below:",
            custom_id="wallet_responce",
            placeholder="0xceb24d38044161c094E9E14cf6F384C19390dd61",
            min_length=42,
            max_length=42,
        )
        insta = interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="Type your instagram username below:",
            custom_id="insta_responce",
            placeholder="@username",
            min_length=1,
            max_length=30,
        )
        tg = interactions.TextInput(
            style=interactions.TextStyleType.SHORT,
            label="Type your telegram username below:",
            custom_id="telegram_responce",
            placeholder="@username",
            min_length=5,
            max_length=32,
        )
        modal = interactions.Modal(
            title="Application Form",
            custom_id="mod_app_form",
            components=[wallet, insta, tg],
        )

        await ctx.popup(modal)

    @interactions.extension_modal("mod_app_form")
    async def register_response(self, ctx, wallet, insta, tg):
        # msg = await ctx.send(f"Validating your information... Please wait...", ephemeral=True)
        wallet_valid = ":x:"
        insta_valid = ":x:"
        tg_valid = ":x:"
        try:
            eth_addr = EthereumAddress(wallet)
            wallet_valid = ":white_check_mark:"
        except Exception as e:
            wallet_valid = ":x:"
        instagram = 'https://www.instagram.com/'
        insta = insta.removeprefix("@")
        x=requests.get(instagram+insta)
        if x.status_code == 200:
            insta_valid = ":white_check_mark:"
        if not insta.startswith("@"): 
            insta = "@" + insta
        res = self.db.write_user(wallet, insta, tg)
        if res == True:
            await ctx.send(f"**Succesfull!...**\nCryptowallet address - {wallet}\nInstagram username  - {insta}\nTelegram UID               - {tg}", ephemeral=True)
        elif res == "alr":
            await ctx.send("**Failed!**\nThis account is already exist!", ephemeral=True)
        elif res == False:
            await ctx.send(f"**Failed!...**\nCryptowallet address - {wallet_valid}\nInstagram username  - {insta_valid}", ephemeral=True)

def setup(client):
    Register(client)