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
		
def pullMusic(folders):	
	""" 
		Walk through the music folders and create song objects.  
		Return an array
	"""
	print "Start!"
	lock = Lock()
	dbQueue = Queue()
	for folder in folders:
		walker = Process(target=worker.walker, args=(folder, dbQueue, lock,))
		walker.start()
	while dbQueue.empty():
		pass
	
	enterdb = Process(target=worker.enterDB, args=(dbQueue, lock,))
	enterdb.start()
	enterdb.join()
	
	print "Done!"
	
def splitComma(value):
	values = []
	splits = value.split(',')
	
	for split in splits:
		values.append(split.strip())
	
	return values