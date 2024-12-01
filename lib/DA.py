import sqlite3
import datetime

databaseName = "../db/current.db"

con = sqlite3.connect(databaseName)

def AddNewNetwork(addresses, description):
    cur = con.cursor()
    data = [
            addresses, description, 0, int(datetime.datetime.utcnow().timestamp())
            ]
    #print (data)
    cur.execute("Insert into network (addresses, description, isdeleted, createddate) values (?, ?, ?, ?)", data)
    con.commit()

def GetNetworks():
    cur = con.cursor()
    rs = cur.execute("select * from network where isdeleted = 0")
    return rs.fetchall()

def EditNetwork(id, addresses, description, isdeleted):
    cur = con.cursor()
    data = [
        addresses, description, isdeleted, id
        ]
    cur.execute("update network set addresses = ?, description = ? isdeleted = ? where id = ?", data)
    con.commit()

def DeleteNetwork(id):
    cur = con.cursor()
    data = [
            id
            ]
    cur.execute("update network set isdeleted = 1 where id = ?", data)
    con.commit()


