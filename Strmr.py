from strmr import parse
from strmr import webserv
from strmr import db
import os.path

def main():
	print "Ready to start?"
	raw_input()
	
	#check database stuff
	if not db.exists():
		db.initdb()
	config = parse.config()
	config.root = os.path.dirname(os.path.abspath(__file__))
	parse.pullMusic(config.musicFolders)
	webserv.startserv(config)

if __name__ == '__main__':
	main()