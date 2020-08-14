# -*- coding: utf-8 -*-
from flask import render_template, current_app


def bad_request(err):
    '''400 Bad Request error handler'''
    current_app.logger.error('Bad request: %s', err)
    return render_template('errors/400.jinja.html', page_title='Bad request'), 400


def not_found():
    '''404 Not Found error handler'''
    return render_template('errors/404.jinja.html', page_title='Not Found'), 404


def internal(err):
    '''500 Internal Server Error error handler'''
    current_app.logger.error('Internal error: %s', err)
    return render_template('errors/5XX.jinja.html', page_title='Internal Error'), 500
