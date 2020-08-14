# -*- coding: utf-8 -*-
from flask import Flask
from config import configurations as cfgs
from get_csr.blueprints.public import public
from get_csr.blueprints.api import api
from get_csr.exceptions import InvalidConfiguraionType
from get_csr.extensions import babel, get_locale, bootstrap
from get_csr import errorhandlers


def create_app(mode: str = 'development'):
    try:
        cfg = cfgs[mode]
    except KeyError:
        raise InvalidConfiguraionType(
            'Unknown configuration type. Available: {}'.format(', '.join(cfgs.keys()))
        )

    app = Flask(__name__)
    app.config.from_object(cfg)
    babel.init_app(app)
    bootstrap.init_app(app)

    app.add_template_global(name='get_locale', f=get_locale)
    app.add_template_global(
        name='get_another_lang',
        f=lambda langs, clang: ''.join(lang for lang in langs if lang != clang)
    )

    app.register_blueprint(public, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api')

    app.register_error_handler(404, errorhandlers.not_found)
    app.register_error_handler(400, errorhandlers.bad_request)
    app.register_error_handler(500, errorhandlers.internal)
    app.register_error_handler(503, errorhandlers.internal)

    return app
