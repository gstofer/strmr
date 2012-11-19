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
		audio  = mp3.MP3(self.fullpath(), ID3=easyid3.EasyID3)
		self.title = audio['title'][0]
		self.artist = audio['artist'][0]
		self.album = audio['album'][0]
		self.track = audio['tracknumber'][0]
		self.year = audio['date'][0]
		self.genre = audio['genre'][0]
		
	def pulltitle(self):
		pass
		
	def pullartist(self):
		pass
		
	def pullalbum(self):
		pass
	
	def pulltrack(self):
		pass
	
	def pullyear(self):
		pass
	
	def pullgenre(self):
		pass

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