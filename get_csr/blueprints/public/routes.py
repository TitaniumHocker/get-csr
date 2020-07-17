# -*- coding: utf-8 -*-
from flask import render_template
from get_csr.blueprints.public import public


@public.route('/')
def index():
    return render_template('index.jinja.html')
