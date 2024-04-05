import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(description="Returns a list of commands")
    async def help(self, interaction: Interaction):
        await interaction.response.send_message("None... as of now ;)")
    
    @nextcord.slash_command(description="Returns bot latency")
    async def ping(self, interaction: Interaction):
        latency = int(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! My latency is {latency}ms.")
    
    @nextcord.slash_command(description="Returns a given users avatar")
    async def avatar(self, interaction: Interaction, member: Member):
        if member is None:
            member = interaction.user
        avatar_url = str(member.avatar.url)
        name = member.name
        embed = nextcord.Embed(title=f"{name}'s Avatar:", color=0x4b5320)
        embed.set_image(avatar_url)
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(description="Returns a given users avatar")
    async def serveravatar(self, interaction: Interaction, member: Member):
        if member is None:
            member = interaction.user
        avatar_url = str(member.guild_avatar.url)
        name = member.name
        embed = nextcord.Embed(title=f"{name}'s Server Avatar:", color=0x4b5320)
        embed.set_image(avatar_url)
        await interaction.response.send_message(embed=embed)
    
def setup(bot):
    bot.add_cog(Information(bot))