from multiprocessing import Queue
from Queue import Empty
import os, time

from strmr import db
from strmr import music

def enterDB(dbQueue, lock):
	"""
		Method used to enter song objects into the database
	"""
	# while the dbQueue is not empty
	while not dbQueue.empty():
		try:
			# acquire the lock
			lock.acquire()
			# attempt to get something out of the queue for 5 seconds
			base, path, file = dbQueue.get(timeout=5)
			lock.release()
			
			# set the songpath
			songpath = os.path.realpath(path)
			
			# create a song object from the songpath, the file and the base 
			# music directory
			song = music.song(path=songpath, filename=file, base=base)
			
			# song.pullInfo gets information from the ID3 tags on the files
			song.pullInfo()
			
			# enter song information into the database
			db.enterSong(song)
			
			# if there are 2 entries left in the queue sleep to allow worker 
			# more time to parse through the folders
			if dbQueue.qsize() < 2:
				print "Sleeping to get more entries"
				time.sleep(3)
		except Empty:
			print "Empty DB Queue"

def walker(folder, dbQueue, lock):
	"""
		Method used to parse through the specified folder
	"""
	
	# set the base to the specified folder
	base = folder
	for (path, dirs, files) in os.walk(folder):
		# filter out anything without mp3 as the extension
		mp3s = filter(lambda x: 'mp3' == x[-3:], files)
		for file in mp3s:
			#acquire the lock
			lock.acquire()
			
			# place a tuple of the base directory, the path of the file, 
			# and the file name into the queue
			dbQueue.put((base, path, file))
			lock.release()