import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("COG | Moderation Loaded")

    # CLEAR
    @discord.slash_command(name="clear",description="Delete messages.")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=None):
        await ctx.channel.purge(limit=int(amount))
        await ctx.respond(f'Deleted {amount} messages.')

    # KICK & BAN COMMAND
    @discord.slash_command(name="kick",description="Kick members.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if reason==None:
            reason = "no reason provided"
        await member.kick(reason=reason)
        await ctx.respond(f"{member.mention} has been kicked for: {reason}")

    @discord.slash_command(name="ban",description="Ban members.")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        if reason==None:
            reason = "no reason provided"
        await member.ban(reason=reason)
        await ctx.respond(f"{member.mention} has been banned for: {reason}")
    
    # LOCKDOWN & UNLOCKDOWN
    @discord.slash_command(name="lockdown",description="Locks the channel.")
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.respond(ctx.channel.mention + " **is now in lockdown.**")

    @discord.slash_command(name="unlockdown",description="Unlocks the channel.")
    @commands.has_permissions(manage_channels=True)
    async def unlockdown(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.respond(ctx.channel.mention + " **is no longer in lockdown.**")


def setup(bot):
    bot.add_cog(moderation(bot))