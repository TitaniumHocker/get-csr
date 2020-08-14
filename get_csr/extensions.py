# -*- coding: utf-8 -*-
from flask import request, current_app, session
from flask_babelex import Babel
from flask_bootstrap import Bootstrap


babel = Babel()
bootstrap = Bootstrap()


@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    if session.get('lang'):
        return session.get('lang')
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])
