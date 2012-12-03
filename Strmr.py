from strmr import parse
from strmr import webserv
from strmr import db
import os.path

def main():
	# testing lines
	print "Ready to start?"
	raw_input()
	
	# check if the database exists
	if not db.exists():
		db.initdb()
	
	# parse configuration from configuration file
	config = parse.config()
	
	# set the root directory to the current working directory
	# used in setting the staticdir root in webserv
	config.root = os.path.dirname(os.path.abspath(__file__))
	
	# parses through the configured music folders.  Waits until 
	# the enterDB process is finished
	parse.pullMusic(config.musicFolders)
	
	# start the webserver
	webserv.startserv(config)

if __name__ == '__main__':
	main()