import discord

def spawnEmbed(pokemon):
    filename = pokemon.species + ".jpg"
    url = "images/" + pokemon.species + ".jpg"
    file = discord.File(url, filename=filename)
    attachment = "attachment://" + filename
    embed = discord.Embed(title="A wild Pokemon has spawned!")
    embed.set_image(url=attachment)
    return file, embed

def caughtEmbed(pokemon):
    embed = discord.Embed(title="You've caught a " + pokemon.species + '!', description = "These are your " + pokemon.species + "'s stats:")
    embed.add_field(name='**IV\'s**', value='HP: ' + str(pokemon.IV[0]) + '\n'
                                        'Atk: ' + str(pokemon.IV[1]) + '\n' 
                                        'Def: ' + str(pokemon.IV[2]) + '\n'
                                        'SpA: ' + str(pokemon.IV[3]) + '\n'
                                        'SpD: ' + str(pokemon.IV[4]) + '\n'
                                        'Spe: ' + str(pokemon.IV[5]) + '\n'
                                        , inline=False)
    embed.add_field(name="**Nature**", value=pokemon.nature, inline=False)
    return embed