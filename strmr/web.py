import cherrypy
import os
from Cheetah.Template import Template

from strmr import db

tempdir = 'data/templates/'


def _tostr(t):
	"""
		returns a unicode string of the template
	"""
	return t.__unicode__()
	
class Player(object):
	"""
		web page for the music player
	"""
	@cherrypy.expose
	def index(self):
		t = Template(file=tempdir + 'player.tmpl')
		return _tostr(t)

class Songs(object):
	"""
		web page for all the songs
	"""
	@cherrypy.expose
	def index(self):
		songs = db.selectSongs()
		t = Template(file=tempdir + 'songs.tmpl')
		t.songs = songs
		return _tostr(t)
	
	@cherrypy.expose
	def play(self, id = None):
		song = db.selectPlay(id)
		t = Template(file=tempdir + 'play.tmpl')
		t.song = song
		return _tostr(t)

class Albums(object):
	"""
		web page for all the albums
	"""
	@cherrypy.expose
	def index(self):
		t = Template(file=tempdir + 'albums.tmpl')
		return _tostr(t)

class Artists(object):
	"""
		web page for all the artists
	"""
	@cherrypy.expose
	def index(self):
		t = Template(file=tempdir + 'artists.tmpl')
		return _tostr(t)

class Root:
	"""
		front page.
	"""
	@cherrypy.expose
	def index(self):
		t = Template(file=tempdir + 'root.tmpl')
		return _tostr(t)

def webinit():
	"""
		creates the web application
	"""
	root = Root()
	root.player = Player()
	root.songs = Songs()
	root.albums = Albums()
	root.artists = Artists()
	
	app = cherrypy.tree.mount(root, '/', 'data/cherrypy.config')
	return app