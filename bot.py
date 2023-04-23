# Frage den Token ab
token = input('Bot token: ')
print('Sollte der Token von ihnen falsch sein, müssen sie die Datei neuausführen und einen richtigen einfügen\n')


# Importiere Nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands


# Erstelle den Bot
bot = commands.Bot()

# Erstelle ein Slashcommand
@bot.slash_command(description='Bentuze diesen Command, um es zu claimen')
async def claim(interaction: Interaction):
    await interaction.response.send_message('Du kannst dein Badge auf https://discord.com/developers/active-developer in wenigen Tagen beanspruchen!')

# Starte den Bot
bot.run(token)