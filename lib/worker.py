from multiprocessing import Queue
import music, os
import Queue

def enterDB(dbQueue, lock):
	while not dbQueue.empty():
		try:
			lock.acquire()
			info = dbQueue.get(True, 5)
			lock.release()
			songpath = os.path.realpath(info[1])
			file = info[0]
			song = music.song(path=songpath, filename=file)
			song.pullInfo()
			print song.title
			#stuff to enter into database
		except Queue.Empty:
			print "Empty DB Queue"
			lock.release()

def walker(folder, dbQueue, lock):
	for (path, dirs, files) in os.walk(folder):
		for file in files:
			lock.acquire()
			dbQueue.put((file, path))
			lock.release()
		for dir in dirs:
			walker(dir, dbQueue, lock)