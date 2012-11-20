#!/usr/bin/python

####
#	importing python modules
####
import ConfigParser, os
import time
from multiprocessing import Queue, Process, Lock

####
#	importing strmr modules
####		
import music
from lib import db
from lib import worker

class config:
	def __init__(self, file="strmr.conf"):
		parser = ConfigParser.SafeConfigParser()
		parser.read(file)
		
		if(parser.getboolean('admin', 'security')):
			self.username = parser.get('admin', username, 0)
			self.password = parser.get('admin', password, 0)
		
		self.musicFolders = splitComma(parser.get('music', 'folder', 0))
		
class watchIO(threading.Thread):
	def run():
		pass

def pullMusic(folders):	
	""" 
		Walk through the music folders and create song objects.  
		Return an array
	"""
	print "Start Parsing Folders!"
	lock = Lock()
	dbQueue = Queue()
	for folder in folders:
		walker = Process(target=worker.walker, args=(folder, dbQueue, lock,))
		walker.start()
	while dbQueue.empty():
		pass
	
	#time.sleep(3)
	
	enterdb = Process(target=worker.enterDB, args=(dbQueue, lock))
	enterdb.start()
	enterdb.join()
	
	print "Done!"
	
def splitComma(value):
	values = []
	splits = value.split(',')
	
	for split in splits:
		values.append(split.strip())
	
	return values

def songSql(sinfo):
	id = 0
	name = 0
	path = 0
	filename = 0
	hash = 0
	album = 0
	artist = 0
	length = 0
	track = 0
	genre = 0
	year = 0
	rating = 0
	
	if sinfo[0]:
		id = sinfo[0]
	if sinfo[1]:
		name = sinfo[1]
	if sinfo[2]:
		path = sinfo[2]
	if sinfo[3]:
		filename = sinfo[3]
	if sinfo[4]:
		hash = sinfo[4]
	if sinfo[5]:
		album = sinfo[5]
	if sinfo[6]:
		artist = sinfo[6]
	if sinfo[7]:
		length = sinfo[7]
	if sinfo[8]:
		track = sinfo[8]
	if sinfo[9]:
		genre = sinfo[9]
	if sinfo[10]:
		year = sinfo[10]
	if sinfo[11]:
		rating = sinfo[11]
	
	song = music.song(id=id, name=name, path=path, filename=filename,
		hash=hash, album=album, artist=artist, length=length, track=track,
		genre=genre, year=year, rating=rating)
	
	return song