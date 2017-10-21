import songs

def configure_routes(app):
	app.add_url_rule('/', 'landing', view_func=songs.view.landing, methods=['GET'])

