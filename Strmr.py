from strmr import parse
from strmr import webserv
import os.path

def main():
	print "Ready to start?"
	raw_input()
	config = parse.config()
	config.root = os.path.dirname(os.path.abspath(__file__))
	parse.pullMusic(config.musicFolders)
	webserv.startserv(config)

if __name__ == '__main__':
	main()