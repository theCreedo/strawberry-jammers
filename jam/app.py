import flask
import json

from flask import g, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
# from flask.ext.cdn import CDN
from flask_sslify import SSLify
# from flask_redis import Redis
import sendgrid
# import jam.settings
from jam import settings
import structlog
import pickle

DB = SQLAlchemy()

# from dishes.models import Dish
from jam.songs.models import Song, SongSet
# import jam.routes
from jam import routes
from jam.songs.genius import *


# def configure_login(app):
#     login_manager = LoginManager()
#     login_manager.init_app(app)
#     login_manager.login_view = 'login'
#     login_manager.login_message = ''

#     @login_manager.user_loader
#     def load_user(id):
#         return User.query.get(int(id))

#     @app.before_request
#     def before_request():
#         g.user = current_user


def configure_logger(app):
    def processor(_, method, event):
        levelcolor = {
            'debug': 32,
            'info': 34,
            'warning': 33,
            'error': 31
        }.get(method, 37)

        return '\x1b[{clr}m{met}\x1b[0m [\x1b[35m{rid}\x1b[0m] {msg} {rest}'.format(
            clr=levelcolor,
            met=method.upper(),
            rid=request.headers.get('X-Request-Id', '~'),
            msg=event.pop('event'),
            rest=' '.join(['\x1b[%sm%s\x1b[0m=%s' % (levelcolor, k.upper(), v)
                           for k, v in event.items()])
        )

    structlog.configure(
        processors=[
            structlog.processors.ExceptionPrettyPrinter(),
            processor
        ]
    )

    logger = structlog.get_logger()

    @app.before_request
    def get_request_id():
        g.log = logger.new()


def setup_error_handlers(app):
    @app.errorhandler(404)
    def page_note_found(error):
        return render_template('/static_pages/404.html', title='Page Not Found',
                               message="That page appear not to exist. Maybe you're looking for our <a href='{}' class='decorate'>homepage</a>?".format(
                                   settings.BASE_URL)), 404

    @app.errorhandler(500)
    def internal_error(error):
        g.log = g.log.bind(error=error)
        g.log.error('New 500 Error: ')
        return render_template('/static_pages/error.html', title='Internal Server Error',
                               message='Something went wrong and we are unable to process this request. Our tech team has been alerted to this error and is working hard to fix it. We appreciate your patience! If this error continues, please email {}'.format(
                                   settings.GENERAL_INFO_EMAIL)), 500


# def populate_db(jam_app):
#     print("populating db")   
#     with open('./jam/pyscripts/allDishes.pickle', 'rb') as handle:
#         allDishes = pickle.load(handle)

#     with open('./jam/pyscripts/dishBitMapDict.pickle', 'rb') as handle:
#         dishBitMapDict = pickle.load(handle)

#     with open('./jam/pyscripts/dishHTMLDict.pickle', 'rb') as handle:
#         dishHTMLDict = pickle.load(handle)

#     for dish_name in allDishes:
#         bitMap = pickle.dumps(dishBitMapDict[dish_name])
#         dishData = {
#             'dish_name': dish_name,
#             'dish_url': dishHTMLDict[dish_name],
#             'dish_bitmap': bitMap
#         }
#         # g.log.info('Creating a Dish')
#         # g.log = g.log.bind(dish_name=dishData['dish_name'])
#         # g.log.info('Creating a new dish')
#         with jam_app.app_context():
#             dish = Dish(dishData)
#             DB.session.add(dish)
#             DB.session.commit()

def populate_db(jam_app):
    
    with jam_app.app_context():
        g = Genius(settings.GENIUS_KEY)
        sets = [['What a beautiful name', '10,000 reasons bless the Lord', 'He is exalted'], ['Touch the sky', 'Oceans']]
        for s in sets:
            sset = SongSet({'name': 'im a songset', 'key': '242iuh', 'songs': []})

            for song in s:
                searchresults = g.search(song)
                # send searchresults to frontend
                # get song entry back
                songentry = g.hitstoreadable(searchresults)[0]
                lyrics = g.get_lyrics(songentry['api_path'])
                songentry['lyrics'] = lyrics
                newsong = Song(songentry)
                sset.songs_join.append(newsong)
                DB.session.add(newsong)
            DB.session.add(sset)
            DB.session.commit()
            

def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(settings)

    DB.init_app(app)

    # redis_store.init_app(app)
    routes.configure_routes(app)
    # configure_login(app)
    configure_logger(app)
    setup_error_handlers(app)

    app.jinja_env.filters['json'] = json.dumps

    # app.config['CDN_DOMAIN'] = settings.CDN_URL
    # app.config['CDN_HTTPS'] = True
    # cdn.init_app(app)

    SSLify(app)
    return app

jam_app = create_app()
# populate_db(jam_app)

