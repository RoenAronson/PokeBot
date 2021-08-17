#the breedBot connection to user

import os
import Pokemon
import pokeList
import random as rand
import discord
import dbconn as dbc
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

prefix = '.'

@client.event
async def on_ready():
    print('Ready!')

currPokemon = None

@client.event
async def on_message(message):
    global prefix
    global currPokemon
    if message.author == client.user:
        return
    authorName = message.author.name
    content = message.content.lower()
    if dbc.incMessages(message.author.id):
        await message.channel.send("Your pokemon has leveled up!")
    if prefix == content[0]:
        #TODO -- create the embed to show the user's pokemon
        if "%spokemon" % (prefix) in content:
            species, level, iv = dbc.getPokemonList(message.author.id)
            for i in range(len(species)):
                await message.channel.send(str(species[i]) + ', ' + str(level[i]) + ', ' + str(iv[i]))
        #TODO -- 'info' shows active pokemon stats
        if "%sinfo" % (prefix) in content:
            pSplit = content
            prefix = pSplit.split()[1]
        # Change prefix
        if "%sprefix" % (prefix) in content:
            pSplit = content
            prefix = pSplit.split()[1]
            await message.channel.send('Prefix changed to ' + prefix)
        # Catch pokemon
        if "%scatch" % (prefix) in content:
            if dbc.userExists(message.author.id):
                preAttemptedName = content
                attemptedName = preAttemptedName.split()[1]
                if attemptedName.lower() == currPokemon.species.lower():
                    await message.channel.send('Congratulations, ' + authorName + ', You\'ve caught a ' + currPokemon.species + '! \n' 
                                            'If you would like to see this pokemon\'s stats, you can\'t yet!') #TODO -- also this
                    dbc.addPokemon(message.author.id, currPokemon)
                    currPokemon = None
            else:
                await message.channel.send('You have not started yet. Type %sstart to begin your journey.' % (prefix))
        # Start playing
        if "%sstart" % (prefix) in content:
            if dbc.userExists(message.author.id):
                await message.channel.send('You have already been added to the Pokemon Breeding Registry.')
            else:
                dbc.addUser(message.author.id)
                await startUser(message)
    elif rand.randint(1,5) == 3:
        newPoke = pokeList.spawnMon()
        currPokemon = newPoke
        embed = discord.Embed(title="A wild Pokemon has spawned!", description="A %s has spawned in the channel." % (newPoke.species))
        embed.add_field(name='**IV\'s**', value='HP: ' + str(newPoke.IV[0]) + '\n'
                                            'Atk: ' + str(newPoke.IV[1]) + '\n' 
                                            'Def: ' + str(newPoke.IV[2]) + '\n'
                                            'SpA: ' + str(newPoke.IV[3]) + '\n'
                                            'SpD: ' + str(newPoke.IV[4]) + '\n'
                                            'Spe: ' + str(newPoke.IV[5]) + '\n'
                                            , inline=False)
        embed.add_field(name="**Nature**", value=newPoke.nature, inline=False)
        await message.channel.send(embed=embed)
        
async def startUser(message):
    ##TODO -- create start menu so people can select a starter pokemon
    await message.channel.send(message.author.name + ', you have been added to the Pokemon Breeding Registry!')
    await message.channel.send('We\'re working on this feature now!')
            

    
    

        
        


    
client.run(TOKEN)