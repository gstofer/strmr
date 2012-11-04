#!/usr/bin/python

import parse, multiprocessing

class strmr:
	def __init__(self):
		config = parse.config()
		parse.pullMusic(config.musicFolders)
