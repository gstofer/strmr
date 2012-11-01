#!/usr/bin/python

####
#	importing python modules
####
import ConfigParser, os

####
#	importing strmr modules
####
import music

class config:
	def __init__(self, file="strmr.conf"):
		parser = ConfigParser.SafeConfigParser()
		parser.read(file)
		
		self.config = {'admin':{}, 'music':{}}
		if(parser.getboolean('admin', 'security')):
			self.config['admin'].update({'username':
				parser.get('admin', username, 0)})
			
			self.config['admin'].update({'password':
				parser.get('admin', password, 0)})
		
		self.config['music'].update({'folder':
			splitComma(parser.get('music', 'folder', 0))})