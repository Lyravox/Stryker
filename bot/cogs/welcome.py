import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import random

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1225750503837925396)
        
        name = member.name
        mention = member.mention
        avatar = member.avatar.url
        
        embed = nextcord.Embed(title=f"Welcome {name}!", color=0x4b5320)
        embed.add_field(name="", value=f"Welcome {mention} to the server! Testy ooga booga.")
        embed.set_thumbnail(avatar)
        
        await channel.send(f"{mention}", embed=embed)
        
def setup(bot):
    bot.add_cog(Welcome(bot))