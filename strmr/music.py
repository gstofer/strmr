#!/usr/bin/python

from lib.mutagen import mp3
from lib.mutagen import easyid3
import hashlib
import os

class song:
	"""
		that for song objects that are pulled from the directories or database
	"""
	def __init__(self, title=0, id=0, path=0, filename=0, hash=0, album=0, 
			artist=0, length=0, track=0, genre=0, year=0, rating=0, base=0):
		self.id = id
		self.title = title
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
		self.base = base
		
		# get the hash automatically
		if filename and path:
			if os.path.exists(self.fullpath()):
				self.pullHash()

	def fullpath(self):
		"""
			returns the full path of the file
		"""
		return self.path + "\\" + self.filename
	
	def urlpath(self):
		"""
			returns the path that will be used to play the song through the 
			web server
		"""
		# lowest directory of the path
		basepath = os.path.basename(self.base)
		
		# gets the relative path by getting the path after the music folder
		relpath = os.path.relpath(self.path, self.base)
		
		# if the songfile is located in the music folder the relpath is .
		if relpath != '.':
			urlpath = "/static/" + basepath + "/" + relpath + "/" + self.filename
		else:
			urlpath = "/static/" + basepath + "/" + self.filename
		return urlpath
	
	def pullHash(self):
		"""
			pulls the hash of the file and sets it in the object
		"""
		md5 = hashlib.md5()
		with open(self.fullpath(), 'rb') as f:
			while True:
				data = f.read(1024)
				if not data:
					break
				md5.update(data)
		self.hash = md5.hexdigest()
	
	def gettype(self):
		"""
			gets the extension of the files
		"""
		file = self.filename
		ext = file[-3:]
		return ext
	
	def pullInfo(self):
		"""
			pulls information from the file using mutagen
		"""
		audio  = mp3.MP3(self.fullpath())
		self.title = self.pulltitle(audio)
		self.artist = self.pullartist(audio)
		self.album = self.pullalbum(audio)
		self.track = self.pulltrack(audio)
		
		# year is an ID3Date object.  Get the string representation of that
		# object
		self.year = self.pullyear(audio).__str__()
		self.genre = self.pullgenre(audio)
		self.length = audio.info.length
		
	def pulltitle(self, audio):
		"""
			pulls the title from the audio file using the TIT2 tag
		"""
		title = ""
		titleTag = ['TIT2']
		for tag in titleTag:
			if tag in audio.keys():
				title = audio[tag].text
				break
		return title
		
	def pullartist(self, audio):
		"""
			pulls the artist from the audio file using TPE1 or TPE2 tag
		"""
		artist = ""
		artistTag = ['TPE1', 'TPE2']
		for tag in artistTag:
			if tag in audio.keys():
				artist = audio[tag].text
				break
		return artist
		
	def pullalbum(self, audio):
		"""
			pulls the album from the audio file using the TALB tag
		"""
		album = ""
		albumTag = ['TALB']
		for tag in albumTag:
			if tag in audio.keys():
				album = audio[tag].text
				break
		return album
	
	def pulltrack(self, audio):
		"""
			pulls the track number from the audio file using the TRCK tag
		"""
		track = ""
		trackTag = ['TRCK']
		for tag in trackTag:
			if tag in audio.keys():
				track = audio[tag].text
				break
		return track
	
	def pullyear(self, audio):
		"""
			pulls the release year using one of several tags
		"""
		year = ""
		yearTag = ['TDRC', 'TDAT', 'TRDA', 'TYER', 'TIME']
		for tag in yearTag:
			if tag in audio.keys():
				year = audio[tag]
				if isinstance(year, list):
					year = year[0]
				break
		return year
	
	def pullgenre(self, audio):
		"""
			pulls the genre from the audio file using the TCON tag
		"""
		genre = ""
		genreTag = ['TCON']
		for tag in genreTag:
			if tag in audio.keys():
				genre = audio[tag].text
				break
		return genre
		
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