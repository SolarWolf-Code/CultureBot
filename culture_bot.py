import discord
from discord import app_commands
import os
import random
from create_csv import create_country_csv

# Environment variables
GUILD_ID = os.environ.get('GUILD_ID')
TOKEN = os.environ.get('TOKEN')

# Discord client
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

def random_country_embed():
    with open("countries.csv") as fr:
        contents = fr.read().splitlines()

    random_country = random.choice(contents)
    # remove line from file
    contents.remove(random_country)
    with open("countries.csv", "w") as fw:
        fw.write("\n".join(contents))

    fields = random_country.split(",")
    name = fields[0]
    capital = fields[1]
    subregion = fields[2]
    population = "{:,}".format(int(fields[3]))
    flag = fields[4]

    # create embed
    embed = discord.Embed(
        title=name,
        description="",
        color=discord.Color.red()
    )
    # add fields
    embed.add_field(name="Capital", value=capital, inline=True)
    embed.add_field(name="Subregion", value=subregion, inline=True)
    embed.add_field(name="Population", value=population, inline=True)

    # add image
    embed.set_image(url=flag)
    return embed


@tree.command(name="rc", description="Picks a random country", guild=discord.Object(id=GUILD_ID))
async def random_country(interaction):
    await interaction.response.send_message(embed=random_country_embed())

@tree.command(name="reset", description="Recreates the country csv file", guild=discord.Object(id=GUILD_ID))
async def reset_csv(interaction):
    # send that the csv has been reset
    # create the csv using the create_country_csv function
    create_country_csv()
    await interaction.response.send_message("The csv has been reset.")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print("CultureBot is online!")


if __name__ == "__main__":
    client.run(TOKEN)
