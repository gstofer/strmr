#!/usr/bin/python

import hashlib

class song:
	def __init__(self, name="", id="", path="", filename="", hash=""):
		self.id = id
		self.name = name
		self.path = path
		self.filename = filename
		self.hash = hash

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