#!/usr/bin/python

import parse, multithreading

class strmr:
	__init__(self):
		config = parse.config()
		parse.pullMusic(config.musicFolders)
