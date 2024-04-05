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
    
    @nextcord.slash_command(description="Returns info about the server")
    async def serverinfo(self, interaction: Interaction):
        server = interaction.guild
        name = server.name
        icon = server.icon.url
        creation = server.created_at.strftime("%b %d %Y - %H:%M ")
        owner = server.owner.mention
        members = server.member_count
        roles = len(server.roles)
        categories = len(server.categories)
        text_channels = len(server.text_channels)
        voice_channels = len(server.voice_channels)
        id = server.id
        
        embed = nextcord.Embed(title=f"{name}", color=0x4b5320)
        embed.add_field(name="Owner", value=f"{owner}")
        embed.add_field(name="Members", value=f"{members}")
        embed.add_field(name="Roles", value=f"{roles}")
        embed.add_field(name="Categories", value=f"{categories}")
        embed.add_field(name="Text Channels", value=f"{text_channels}")
        embed.add_field(name="Voice Channels", value=f"{voice_channels}")
        embed.set_footer(icon_url=icon, text=f"ID: {id} | Created • {creation}")
        embed.set_thumbnail(icon)
        
        await interaction.response.send_message(embed=embed)

    
    @nextcord.slash_command(description="Returns the given users avatar")
    async def avatar(self, interaction: Interaction, member: Member):
        if member is None:
            member = interaction.user
        avatar_url = str(member.avatar.url)
        name = member.name
        embed = nextcord.Embed(title=f"{name}'s Avatar:", color=0x4b5320)
        embed.set_image(avatar_url)
        await interaction.response.send_message(embed=embed)
    
def setup(bot):
    bot.add_cog(Information(bot))