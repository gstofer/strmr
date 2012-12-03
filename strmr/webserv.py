import web
import cherrypy
import os.path

def startserv(config):
	"""
		starts the web server
	"""
	# create the web app
	app = web.webinit()

	# set the root static directory
	conf = { '/' : {'tools.staticdir.root': config.root}}
	
	# set each music folder to be a static directory
	for folder in config.musicFolders:
		base = os.path.basename(os.path.normpath(folder))
		conf.update({ '/static/' + base: {'tools.staticdir.on': True,
						'tools.staticdir.dir': folder}
			})

	# merge the app configuration file with the dictionary one that
	# was created
	app.merge(conf)
	
	# create the configuration for the web server
	cherrypy.config.update(conf)
	cherrypy.config.update('data/cherrypy.config')
	
	if hasattr(cherrypy.engine, "signal_handler"):
		cherrypy.engine.signal_handler.subscribe()
	if hasattr(cherrypy.engine, "console_control_handler"):
		cherrypy.engine.console_control_handler.subscribe()
	cherrypy.engine.start()
	cherrypy.engine.block()
	#cherrypy.quickstart(root=app, config='data/cherrypy.config')