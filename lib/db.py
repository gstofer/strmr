import sqlite3
	
def initdb():
	conn = sqlite3.connect('data\\strmr.db')
	c = conn.cursor()
	with open('r', 'data\\database.sql') as f:
		for line in f:
			c.execute(line)

def connect():
	conn = sqlite3.connect('data\\strmr.db')
	return conn
