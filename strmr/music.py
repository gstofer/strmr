#!/usr/bin/python

from lib.mutagen import mp3
from lib.mutagen import easyid3
import hashlib

class song:
	def __init__(self, name=0, id=0, path=0, filename=0, hash=0, album=0, 
			artist=0, length=0, track=0, genre=0, year=0, rating=0):
		self.id = id
		self.name = name
		self.path = path
		self.filename = filename
		self.hash = hash
		self.album = album
		self.artist = artist
		self.length = length
		self.track = track
		self.genre = genre
		self.year = year
		self.rating = rating

	def fullpath(self):
		return self.path + "\\" + self.filename
	
	def pullHash(self):
		md5 = hashlib.md5()
		with open(self.fullpath(), 'rb') as f:
			while True:
				data = f.read(1024)
				if not data:
					break
				md5.update(data)
		self.hash = md5.hexdigest()
	
	def pullInfo(self):
		audio  = mp3.MP3(self.fullpath())
		self.title = audio['title'][0]
		self.artist = self.pullartist(audio)
		self.album = audio['album'][0]
		self.track = audio['tracknumber'][0]
		self.year = audio['date'][0]
		self.genre = audio['genre'][0]
		
	def pulltitle(self):
		pass
		
	def pullartist(self, audio):
		artist = ""
		artistTag = ['TPE1', 'TPE2']
		for tag in artistTag:
			if tag in audio.keys()
				artist = audio[tag].text
				break
		return artist
		
	def pullalbum(self):
		pass
	
	def pulltrack(self):
		pass
	
	def pullyear(self):
		pass
	
	def pullgenre(self):
		pass
		
	def songSql(sinfo):
		self.id = 0
		self.name = 0
		self.path = 0
		self.filename = 0
		self.hash = 0
		self.album = 0
		self.artist = 0
		self.length = 0
		self.track = 0
		self.genre = 0
		self.year = 0
		self.rating = 0
		
		if sinfo[0]:
			self.id = sinfo[0]
		if sinfo[1]:
			self.name = sinfo[1]
		if sinfo[2]:
			self.path = sinfo[2]
		if sinfo[3]:
			self.filename = sinfo[3]
		if sinfo[4]:
			self.hash = sinfo[4]
		if sinfo[5]:
			self.album = sinfo[5]
		if sinfo[6]:
			self.artist = sinfo[6]
		if sinfo[7]:
			self.length = sinfo[7]
		if sinfo[8]:
			self.track = sinfo[8]
		if sinfo[9]:
			self.genre = sinfo[9]
		if sinfo[10]:
			self.year = sinfo[10]
		if sinfo[11]:
			self.rating = sinfo[11]
		
#		song = music.song(id=id, name=name, path=path, filename=filename,
#			hash=hash, album=album, artist=artist, length=length, track=track,
#			genre=genre, year=year, rating=rating)
		
		return self

class artist:
	def __init__(self, name="", id=""):
		"""
			artist class that has an artist ID, the artist name, and an array
			of album objects
		"""
		self.id = ""
		self.albums = []
		self.name = name

class album:
	def __init__(self, name="", year="", artist=""):
		"""
			album class which has the name of the album, year it came out
			and the artist that wrote it.
		"""
		self.id = ""
		self.name = name
		self.songs = []
		self.year = year	