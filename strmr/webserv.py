import web
import cherrypy
import os.path

def startserv(config):
	app = web.webinit()

	conf = { '/' : {'tools.staticdir.root': config.root}}
	
	for folder in config.musicFolders:
		base = os.path.basename(os.path.normpath(folder))
		conf.update({ '/static/' + base: {'tools.staticdir.on': True,
						'tools.staticdir.dir': folder}
			})

	app.merge(conf)
	
	cherrypy.config.update(conf)
	cherrypy.config.update('data/cherrypy.config')
	
	if hasattr(cherrypy.engine, "signal_handler"):
		cherrypy.engine.signal_handler.subscribe()
	if hasattr(cherrypy.engine, "console_control_handler"):
		cherrypy.engine.console_control_handler.subscribe()
	cherrypy.engine.start()
	cherrypy.engine.block()
	#cherrypy.quickstart(root=app, config='data/cherrypy.config')