from logging import NullHandler, raiseExceptions
import pyodbc 
import uuid

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=localhost;'
                      'Database=pokemon;'
                      'Trusted_Connection=yes;')


curs = conn.cursor()

def userExists(userID):
    curs.execute("select count(*) user_id from users where user_id = ?", userID)
    result = curs.fetchone()[0]
    return result == 1

def addUser(userID):
    userID = int(userID)
    print(userID)
    curs.execute("exec add_user @userID = ?", userID)
    curs.commit()

def addPokemon(userID, p):
    poke_iv = uuid.uuid4()
    poke_moves_id = uuid.uuid4()
    poke_nickname = ""
    poke_base_stats_id = uuid.uuid4()
    poke_ev_id = uuid.uuid4()
    poke_stats_id = uuid.uuid4()

    curs.execute("insert into trainer_pokemon values (?,?,?,?,?,?,?,?,?,?,?,?,?)", (p.uniqueID, p.speciesID, poke_iv, poke_moves_id, poke_nickname, 
                                                                         p.heldItem, p.nature, poke_base_stats_id,
                                                                         poke_ev_id, p.level, userID, p.gender, poke_stats_id))
    curs.execute("insert into base_stats values (?,?,?,?,?,?,?)", (p.uniqueID, p.baseStats[0],p.baseStats[1],p.baseStats[2],p.baseStats[3],p.baseStats[4],p.baseStats[5]))
    curs.execute("insert into iv_stats values (?,?,?,?,?,?,?)", (p.uniqueID, p.IV[0],p.IV[1],p.IV[2],p.IV[3],p.IV[4],p.IV[5]))
    curs.execute("insert into ev_stats values (?,?,?,?,?,?)", (p.uniqueID, p.EV[1],p.EV[2],p.EV[3],p.EV[4],p.EV[5]))
    curs.execute("insert into calculated_stats values (?,?,?,?,?,?,?)", (p.uniqueID, p.stats[0],p.stats[1],p.stats[2],p.stats[3],p.stats[4],p.stats[5]))
    curs.commit()