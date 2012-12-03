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
from strmr import music
from strmr import worker

class config:
	"""
		Parse through the specified configuration file
	"""
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
	print "Start Parsing Folders!"
	lock = Lock()
	dbQueue = Queue()
	
	# create a process for each music folder in the configuration file
	for folder in folders:
		walker = Process(target=worker.walker, args=(folder, dbQueue, lock,))
		walker.start()
	while dbQueue.empty():
		pass
	
	# create a process to enter files from the dbQueue into the database
	enterdb = Process(target=worker.enterDB, args=(dbQueue, lock))
	enterdb.start()

	# wait until enterDB is finished before starting
	# This can be taken out later.  I want complete information for testing
	enterdb.join()
	
	print "Done!"
	
def splitComma(value):
	"""
		used to parse the music folders
	"""
	values = []
	splits = value.split(',')
	
	for split in splits:
		values.append(split.strip())
	
	return values