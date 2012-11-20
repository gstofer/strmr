import sqlite3

import music
	
def initdb():
	c, conn = connect()
	sql = []
	with open('data\\database.sql') as f:
		for line in f:
			sql.append(line.strip())
	
	for query in sql:
		c.execute(query)
	conn.commit()

def enterSong(song):
	c, conn = connect()
	sql = []

	if checkHash(song):
		appendSong(song)
	
		if song.artist:
			sql2 = appendArtist(song)
			sql += sql2
	
		if song.album:
			sql2 = appendAlbum
			sql += sql2
	
	for query in sql:
		c.execute(query)
	conn.commit()

def checkHash(song):
	sql = "Select path, filename, hash from songs where hash = '" + song.hash + "';"
	c, conn = connect()
	c.execute(sql)
	path, file, hash = c.fetchone()
	if hash == song.hash:
		return False
	else:
		return True
	
def appendSong(song):
	sql = []
	sql.append("INSERT INTO SONGS (filename, path, hash) VALUES ('" 
		+ song.filename + "', '" + song.path + "', '" + song.hash + "');")
	return sql
	
def appendArtist(song):
	sql = []
	
	sql.append("INSERT INTO ARTIST ('name') VALUES ('" 
	+ song.artist + "');")
	
	sql.append("INSERT INTO songs_artist ('songs_id', 'artist_id')"
	+ " VALUES ((select id from songs where hash = '" + song.hash + "'), "
	+ "(select id from artist where name = '" + song.artist + "'));")
	
	return sql
	
def appendAlbum(song):
	sql = []
	sql.append("INSERT INTO ALBUM ('name') VALUES ('" 
	+ song.album + "');")
	
	sql.append("INSERT INTO songs_album ('songs_id, album_id')"
	+ " VALUES ((select id from songs where hash = '" + song.hash + "'), "
	+ "(select id from album where name = '" + song.album + "'));")
	
	return sql
	
def connect():
	conn = sqlite3.connect('data\\strmr.db')
	c = conn.cursor()
	return c, conn
