import discord
from discord.ext import commands
from core.core import Cog_Extension
from oriana.oriana import clear_chat

class cmds(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(title=f"{member.name}的頭貼", color=0x00ff00)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def clear_chat(self, ctx):
      res = clear_chat(str(ctx.channel.id))
      if res:
        await ctx.send('已清除')
      else:
        await ctx.send('沒有記錄可以清除')

async def setup(bot):
    await bot.add_cog(cmds(bot))