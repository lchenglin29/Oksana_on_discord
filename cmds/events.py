import discord
from discord.ext import commands
from core.core import Cog_Extension
from oriana.oriana import calling_Oriana

class event(Cog_Extension):
  @commands.Cog.listener()
  async def on_message(self,message):
    if message.author == self.bot.user:
      return
    if self.bot.user.mention in message.content:
      await message.reply(calling_Oriana(message.content,message.channel.id))
  @commands.Cog.listener()
  async def on_member_join(self,member:discord.Member):
    channel = self.bot.get_channel(1202596441088987156)
    if member.guild.id == 1202596440535343154:
      await channel.send(f'{member.mention}，歡迎來到{member.guild.name}！\n你可以看 <#1202599065318326272> 了解O-bot的玩法\n若要開始遊戲，請到 <#1203004488340742214> 使用指令！')

async def setup(bot):
    await bot.add_cog(event(bot))