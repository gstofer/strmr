from strmr import parse
from strmr import webserv

def main():
	print "Ready to start?"
	raw_input()
	config = parse.config()
	parse.pullMusic(config.musicFolders)
	webserv.startserv()

if __name__ == '__main__':
	main()