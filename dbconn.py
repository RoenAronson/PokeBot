from logging import NullHandler, raiseExceptions
import Pokemon
import pyodbc 
import uuid

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=localhost;'
                      'Database=pokemon;'
                      'Trusted_Connection=yes;')


curs = conn.cursor()

def userExists(userID):
    curs.execute("select count(*) trainer_id from trainers where user_id = ?", userID)
    result = curs.fetchone()[0]
    return result == 1

def addUser(userID):
    userID = int(userID)
    print(userID)
    curs.execute("insert into trainers values (?, Null)", userID)
    curs.commit()

def addPokemon(userID, p):
    poke_iv = uuid.uuid4()
    poke_moves_id = uuid.uuid4()
    poke_nickname = ""
    poke_base_stats_id = uuid.uuid4()
    poke_ev_id = uuid.uuid4()
    poke_stats_id = uuid.uuid4()

    curs.execute("select count(*) from trainer_pokemon where tp_trainer_id = ?", userID)
    result = curs.fetchone()[0]
    print(result)
    curs.execute("insert into trainer_pokemon values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (p.uniqueID, p.speciesID, poke_iv, poke_moves_id, poke_nickname, 
                                                                         p.heldItem, p.nature, poke_base_stats_id,
                                                                         poke_ev_id, p.level, userID, p.gender, poke_stats_id, 0))
    curs.execute("insert into base_stats values (?,?,?,?,?,?,?)", (p.uniqueID, p.baseStats[0],p.baseStats[1],p.baseStats[2],p.baseStats[3],p.baseStats[4],p.baseStats[5]))
    curs.execute("insert into iv_stats values (?,?,?,?,?,?,?)", (p.uniqueID, p.IV[0],p.IV[1],p.IV[2],p.IV[3],p.IV[4],p.IV[5]))
    curs.execute("insert into ev_stats values (?,?,?,?,?,?)", (p.uniqueID, p.EV[1],p.EV[2],p.EV[3],p.EV[4],p.EV[5]))
    curs.execute("insert into calculated_stats values (?,?,?,?,?,?,?)", (p.uniqueID, p.stats[0],p.stats[1],p.stats[2],p.stats[3],p.stats[4],p.stats[5]))
    curs.commit()
    
    if result == 0:
        curs.execute("update trainers set active_pokemon_id = ? where user_id = ?", p.uniqueID, userID)
        curs.commit()

def incMessages(userID):
    printMessage = False
    curs.execute("select tp_level, tp_poke_id, tp_xp from trainer_pokemon where tp_poke_id in (select active_pokemon_id from trainers where user_id like ?)", userID)
    result = curs.fetchone()
    if result:
        pokemonLevel = result[0]
        print(pokemonLevel)
        poke_id = result[1]
        messageCount = result[2]
        if messageCount >= pokemonLevel**3:
            newlevel = pokemonLevel + 1
            curs.execute("update trainer_pokemon set tp_level = ? where tp_poke_id = ?", (newlevel, poke_id))
            updateStats(poke_id, pokemonLevel)
            printMessage = True
        messageCount += 1
        curs.execute("update trainer_pokemon set tp_xp = ? where tp_poke_id = ?", (messageCount, poke_id))
        curs.commit()
    return printMessage
    
def updateStats(pokeID, level):
    curs.execute("select * from iv_stats where iv_poke_id = ?", pokeID)
    iv = []
    ev = [0]
    bs = []
    result = curs.fetchone()
    for i in range(1,7):
        iv.append(result[i])
    curs.execute("select * from ev_stats where ev_pokemon_id = ?", pokeID)
    for i in range(1,6):
        ev.append(result[i])
    curs.execute("select * from base_stats where bs_pokemon_id = ?", pokeID)
    for i in range(1,7):
        bs.append(result[i])
    curs.execute("select tp_nature from trainer_pokemon where tp_poke_id = ?", pokeID)
    nature = curs.fetchone()[0]
    stats = Pokemon.calculateStats(iv, ev, bs, nature, level)
    sql = """update calculated_stats set cs_hp = ?, 
            cs_atk = ?, cs_def = ?, cs_spa = ?, cs_spd = ?, cs_spe = ? 
            where cs_poke_id = ?"""
    curs.execute(sql, (stats[0],stats[1],stats[2],stats[3],stats[4],stats[5],pokeID))
    curs.commit()

def getPokemonList(userID):
    species = []
    level = []
    iv = []
    curs.execute("""select tp_species, tp_level, iv_hp, iv_atk, iv_def, iv_spa, iv_spd, iv_spe from trainer_pokemon 
                   join iv_stats on iv_poke_id = tp_poke_id 
                   where tp_trainer_id = ?""", userID)
    for row in curs.fetchall():
        species.append(row[0])
        level.append(row[1])
        iv.append([row[2],row[3],row[4],row[5],row[6],row[7]])
    return species, level, iv
    