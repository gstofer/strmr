import cherrypy
import os
from Cheetah.Template import Template

tempdir = 'data/templates/'


def _tostr(t):
	return t.__unicode__()
	
class Player(object):
	@cherrypy.expose
	def index(self):
		t = Template(file=tempdir + 'player.tmpl')
		return _tostr(t)

class Songs(object):
	@cherrypy.expose
	def index(self):
		t = Template(file=tempdir + 'songs.tmpl')
		return _tostr(t)

class Albums(object):
	@cherrypy.expose
	def index(self):
		t = Template(file=tempdir + 'albums.tmpl')
		return _tostr(t)

class Artists(object):
	@cherrypy.expose
	def index(self):
		t = Template(file=tempdir + 'artists.tmpl')
		return _tostr(t)

class Root:
	@cherrypy.expose
	def index(self):
		t = Template(file=tempdir + 'root.tmpl')
		return _tostr(t)

def webinit():
	root = Root()
	root.player = Player()
	root.songs = Songs()
	root.albums = Albums()
	root.artists = Artists()
	
	app = cherrypy.tree.mount(root, '/', 'data/cherrypy.config')
	return app