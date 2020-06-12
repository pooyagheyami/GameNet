# In the name of God
#! use/bin/env python

import wxdb as db
from Config.Init import *


class SQLite(object):
    def __init__(self,tabels,fields,values):
        self.tabels=tabels
        self.fields=fields
        self.values=values

    def create(self,**karg):
        pass

    def insert(self,**karg):
        sql = 'insert into '+str(self.tabels)
        sql = sql+ '('+str(self.fields)+')'
        
        
        sql = sql +' values '+'('+'?,'*(len(self.fields.split(','))-1)+'?)'
        
        #print sql
        return sql

    def select(self,*arg,**karg):
        
        sql =  ' select '+self.fields+' from '+self.tabels
        #print sql
        return sql

    def select1(self,*arg,**karg):
        
        sql =  ' select '+self.fields+' from '+self.tabels+' where '+self.values
        #print sql
        return sql

    def update(self,**karg):

        sql = ' update '+self.tabels+' set '+self.fields
        #print sql
        return sql

    def delete(self,**karg):
        pass
    
def MyDB_Path(database):
    global MAP
    global SLASH
    global DATABASE_PATH
    return db.WXDB(database,MAP+SLASH+DATABASE_PATH+SLASH)


def wxsqsel(database,tabels,fields='*',condition=''):
    global MAP
    #print MAP
    #print database,tabels,fields,condition
        
    Mydb = MyDB_Path(database)
    Mydb.connect()
    sql = SQLite(tabels,fields,condition)
    sql1 = sql.select(fields,tabels)
       
    mylist = Mydb.execute(sql1)
    return mylist


def wxsqltxt(database,text):
    global MAP
    Mydb = MyDB_Path(database)
    mylist = Mydb.execute(text)
    return mylist
    
def wxsqins(database,tabels,fields,data):
    global MAP
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields,values=data)
    sql1 = sql.insert()
    #print sql
    mylist = Mydb.execone(sql1,data)
    Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist
    
def wxsqlup(database,tabels,fields,data):
    global MAP
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields,values=data)
    sql1 = sql.update()
    #print sql
    #print sql1
    mylist = Mydb.execone(sql1,data)
    Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist 





    
