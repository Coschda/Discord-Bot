import discord, os
from discord.ext import commands


class CustomHelpCommand(commands.HelpCommand):

   def __init__():
      super().__init__()
   
   async def send_bot_help(self, mapping):
      return await super().send_bot_help(mapping)

   async def send_cog_help(self, cog):
      return await super().send_cog_help(cog)
   
   async def send_group_help(self, group):
      return await super().send_group_help(group)

   async def send_command_help(self, command):
      return await super().send_command_help(command)
      

intents = discord.Intents.all()
#intents member
client = commands.Bot(command_prefix="$", intents=intents, help_command=CustomHelpCommand())


for filename in os.listdir('./Discord Bot/Bot/cogs'):
   if filename.endswith('.py'):
      client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def load(ctx, extension):
   client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
   client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
   client.unload_extension(f'cogs.{extension}')
   client.load_extension(f'cogs.{extension}')

@client.event
async def on_ready():
   await client.change_presence(status=discord.Status.dnd, activity=discord.Game("C'est moi uesh"))
   print('Bot connecté.')

client.run('OTQ0NjM2OTA1NjY3MDM5Mjcz.YhEfrA.mC3517lQQ-SlE3AQp-NL4n4A1dg')