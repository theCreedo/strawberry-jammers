from jam import songs

def configure_routes(app):
	app.add_url_rule('/', 'landing', view_func=songs.views.landing, methods=['GET', 'POST'])
	# app.add_url_rule('/getSongName', 'getSongNames', view_func=songs.views.landing, methods=['GET'])
