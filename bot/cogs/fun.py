import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(description="Roll some dice")
    async def roll(self, interaction: Interaction, sides: int = SlashOption(description="Number of sides on the dice", required=False)):
        if sides is None:
            sides = 6
        result = random.randint(1, sides)
        await interaction.response.send_message(f"{result}")
            
        
def setup(bot):
    bot.add_cog(Fun(bot))