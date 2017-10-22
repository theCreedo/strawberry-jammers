from flask import request, render_template, redirect, url_for, flash, g
from flask.ext.login import current_user, login_required, login_user, logout_user
from jam.app import DB
from jam.songs.models import Song
from jam.users.models import User
import random
import pickle
from jam.songs.views import Song
from jam.users.helpers import check_password, hash_pwd
import requests
import urllib,json
from sqlalchemy import distinct


def landing():
	if request.method == 'GET':
		song_names = DB.session.query(distinct(Song.name)).all()
		# song_names = [filter(lambda x: x[0] is not None, filter_list) for filter_list in
		#                                     [song_names]]
		# song_names = [map(lambda x: x[0], filter_list) for filter_list in
		#                                     [song_names]]
		song_names.sort()
		return render_template("static_pages/index.html", current_user=current_user, song_names=song_names)
	else:
		song_names = DB.session.query(distinct(Song.name)).all()
		song_names.sort()
		return render_template("static_pages/index.html", current_user=current_user, song_names=song_names)

# def getSongNames():
# 	song_name = ["Sweetly Broken", "How Great Is Our God"]
# 	return song_name


def error404():
	return render_template("static_pages/404.html")

def error500():
	return render_template("static_pages/error.html")

@login_required
def logout():
    logout_user()
    return redirect(url_for('landing'))

@login_required
def profile():
	if not current_user.prev_dish is None:
		return render_template("users/profile.html", dish=pickle.loads(current_user.prev_dish), current_user=current_user)
	else:
		return render_template("users/profile.html", dish=None, current_user=current_user)


# @login_required
# def update_user(user):
# 	DB.session.add(user)
# 	DB.session.commit()



