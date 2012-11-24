import sqlite3

from strmr import music
	
def initdb():
	c, conn = connect()
	sql = []
	with open('data\\database.sql') as f:
		for line in f:
			sql.append(line.strip())
	
	for query in sql:
		c.execute(query)
	conn.commit()

def selectSong(id):
	sql = "SELECT * FROM SONG WHERE id = " + id + ";"
	c, conn = connect()
	c.execute(sql)
	sinfo = c.fetchone()
	song = music.song.songSql(sinfo)
	return song
	
def enterSong(song):
	c, conn = connect()
	sql = []

	if checkHash(song):
		sql2 = appendSong(song)
		sql += sql2
		
		if song.artist:
			sql2 = appendArtist(song)
			sql += sql2
	
		if song.album:
			sql2 = appendAlbum
			sql += sql2
	
	for query in sql:
		c.execute(query)
	conn.commit()
	return sql

def checkHash(song):
	sql = "Select path, filename, hash from songs where hash = '" + song.hash + "';"
	c, conn = connect()
	c.execute(sql)
	notexists = True
	for (path, filename, hash) in c:
		if hash == song.hash:
			notexists = False
		else:
			notexists = True
	return notexists
	
	
def appendSong(song):
	sql = []
	sql.append("INSERT INTO SONGS (filename, path, hash, length, track, "
		+ "genre, year) VALUES ('" + song.filename + "', '" + song.path 
		+ "', '" + str(song.hash) + ", '" + str(song.length) + "', '" 
		+ '/'.join(str(song.track)) + "', '" + '/'.join(str(song.genre)) 
		+ "', '" + str(song.year) + "');")
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
	
	sql.append("INSERT INTO songs_album ('songs_id', 'album_id')"
	+ " VALUES ((select id from songs where hash = '" + song.hash + "'), "
	+ "(select id from album where name = '" + song.album + "'));")
	sql.append("INSERT INTO artist_album ('artist_id', 'album_id')"
	+ " VALUES ((select id from songs where hash = '" + song.hash + "'), "
	+ "(select id from album where name = '" + song.album + "'));")
	
	return sql
	
def connect():
	conn = sqlite3.connect('data\\strmr.db')
	c = conn.cursor()
	return c, conn
