#!/usr/bin/python

import parse, multiprocessing

class strmr:
	def __init__(self):
		print "Ready to start?"
		raw_input()
		config = parse.config()
		parse.pullMusic(config.musicFolders)

if __name__ == '__main__':
	strm = strmr()