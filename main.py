import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# DECLERATIONS
load_dotenv() 
bot = discord.Bot(command_prefix=".")

# STARTUP
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type=discord.ActivityType.watching, name="over the server."))
    print("BOT | Status changed.")

# ERROR HANDLING
@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.respond(embed=discord.Embed(color=discord.Color.red(), description=f":x: Missing required argument."))
    if isinstance(error, commands.MissingPermissions):
        await ctx.respond(embed=discord.Embed(color=discord.Color.red(), description=f":x: You do not have the required permissions."))

# HELP COMMAND
@bot.slash_command(name="help",description="Lists all the commands of the bot.")
async def help(ctx):
    embed = discord.Embed(title="Commands:", color=discord.Color.purple()) 
    embed.add_field(name="Moderation", value="Kick - .kick @member reason\n Ban - .ban @member reason\n Unban - .unban @member\n Clear - .clear amount", inline=False)
    embed.add_field(name="Miscellaneous", value="Ping - not working", inline=False)
    embed.add_field(name="Lockdown", value="Lockdown - .lockdown (locks channel)\n Unlockdown - .unlockdown (unlocks channel)", inline=False)
    await ctx.respond(embed=embed) 

# PING
@bot.slash_command(description="Client to Server latency")
async def ping(ctx):
    await ctx.respond(f'Around {round(bot.latency * 1000)}ms')

# LOAD COGS / STARTUP
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension("cogs." + filename[:-3])

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))