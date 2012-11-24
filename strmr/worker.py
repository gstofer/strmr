from multiprocessing import Queue
from Queue import Empty
import os, time

from strmr import db
from strmr import music

def enterDB(dbQueue, lock):
	while not dbQueue.empty():
		try:
			lock.acquire()
			path, file = dbQueue.get(timeout=5)
			lock.release()
			songpath = os.path.realpath(path)
			song = music.song(path=songpath, filename=file)
			song.pullHash()
			song.pullInfo()
			# print song.filename
			
			# stuff to enter into database
			db.enterSong(song)
			if dbQueue.qsize() < 2:
				print "Sleeping to get more entries"
				time.sleep(3)
		except Empty:
			print "Empty DB Queue"

def walker(folder, dbQueue, lock):
	for (path, dirs, files) in os.walk(folder):
		mp3s = filter(lambda x: 'mp3' == x[-3:], files)
		for file in mp3s:
			lock.acquire()
			dbQueue.put((path, file))
			lock.release()