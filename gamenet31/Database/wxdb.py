# In the name of God
#! use/bin/env python

import sqlite3
import os

class WXDB(object):
    def __init__(self,database=":memory:",pathdb=os.getcwd()):
        self.database=pathdb+database
        #print pathdb
        self.connect()

    def connect(self):
        #print self.database
        try :
           self.connection=sqlite3.connect(self.database)
           self.cursor=self.connection.cursor()
        except:
           print 'No Database find'
        self.connected=True
        self.statement=''
        return self.connection

    def close(self):
        self.connection.commit()
        self.connection.close()
        self.connected=False


    def commit(self):
        return self.connection.commit()
        
    def execute(self,statments):
        #with self.connect():
        self.cursor.execute(statments)
        result = self.cursor.fetchall()
        return result
    
    def execone(self,statments,*data):
        #with self.connect():
        #print statments
        #print data,data[0],data[0][0]
        if data == None:
            self.cursor.execute(statments)
        else:
            self.cursor.execute(statments,data[0])
        result = self.cursor.fetchall()
        #print result
        return result 
