from multiprocessing import Queue
import os, time

from lib import helper
from lib import db
import music

def enterDB(dbQueue, lock):
	while not dbQueue.empty():
		try:
			lock.acquire()
			path, file = dbQueue.get(timeout=5)
			lock.release()
			songpath = os.path.realpath(path)
			md5hash = md5Checksum(songpath, file)
			song = music.song(path=songpath, filename=file, hash=md5hash)
			# song.pullInfo()
			# print song.filename
			# stuff to enter into database
			db.enterSong(song)
			if dbQueue.qsize() < 2:
				print "Sleeping to get more entries"
				time.sleep(3)
		except Queue.Empty:
			print "Empty DB Queue"

def walker(folder, dbQueue, lock):
	for (path, dirs, files) in os.walk(folder):
		mp3s = filter(lambda x: 'mp3' == x[-3:], files)
		for file in mp3s:
			lock.acquire()
			dbQueue.put((file, path))
			lock.release()