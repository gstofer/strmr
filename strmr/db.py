import sqlite3
import os

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

def exists():
	return os.path.exists('data/strmr.db')

def selectSongs():
	sql ="select songs.title, artist.name, album.name from songs, album, " \
	+ "artist join songs_album on songs.id=songs_album.songs_id " \
	+ "join songs_artist on songs.id=songs_artist.songs_id " \
	+ "where album.id=songs_album.album_id " \
	+ "and artist.id=songs_artist.artist_id"
	c, conn = connect()
	retr = c.execute(sql)
	songs = []
	for entry in retr:
		songs.append(music.song(title=entry[0], artist=entry[1], album=entry[2]))
	return songs
	
def selectPlay(id):
	song = music.song()
	sql = "SELECT id, name, path, filename, hash FROM songs " \
		+ "WHERE id = " + id + ";"
	c, conn = connect()
	c.execute(sql)
	sinfo = c.fetchone()
	
	if sinfo[0]:
		song.id = sinfo[0]
	if sinfo[1]:
		song.name = sinfo[1]
	if sinfo[2]:
		song.path = sinfo[2]
	if sinfo[3]:
		song.filename = sinfo[3]
	if sinfo[4]:
		song.hash = sinfo[4]
	
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
			sql2 = appendAlbum(song)
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
		+ "genre, date, title) VALUES ('" + song.filename + "', '" + song.path 
		+ "', '" + str(song.hash) + "', '" + str(song.length) + "', '" 
		+ '/'.join(song.track) + "', '" + '/'.join(song.genre) 
		+ "', '" + str(song.year) + "', '" + '/'.join(song.title) + "');")
	return sql
	
def appendArtist(song):
	sql = []
	
	sql.append("INSERT INTO ARTIST ('name') VALUES ('" 
	+ '/'.join(song.artist) + "');")
	
	sql.append("INSERT INTO songs_artist ('songs_id', 'artist_id')"
	+ " VALUES ((select id from songs where hash = '" + str(song.hash) + "'), "
	+ "(select id from artist where name = '" + '/'.join(song.artist) + "'));")
	
	return sql
	
def appendAlbum(song):
	sql = []
	sql.append("INSERT INTO ALBUM ('name') VALUES ('" 
	+ '/'.join(song.album) + "');")
	
	sql.append("INSERT INTO songs_album ('songs_id', 'album_id')"
	+ " VALUES ((select id from songs where hash = '" + str(song.hash) + "'), "
	+ "(select id from album where name = '" + '/'.join(song.album) + "'));")
	sql.append("INSERT INTO artist_album ('artist_id', 'album_id')"
	+ " VALUES ((select id from songs where hash = '" + str(song.hash) + "'), "
	+ "(select id from album where name = '" + '/'.join(song.album) + "'));")
	
	return sql
	
def connect():
	conn = sqlite3.connect('data\\strmr.db')
	c = conn.cursor()
	return c, conn
