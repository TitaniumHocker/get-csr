# -*- coding: utf-8 -*-
from flask import Flask
from config import configurations as cfgs
from get_csr.exceptions import InvalidConfiguraionType
from get_csr.extensions import babel
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

    app.register_error_handler(404, errorhandlers.not_found)
    app.register_error_handler(400, errorhandlers.bad_request)
    app.register_error_handler(500, errorhandlers.internal)
    app.register_error_handler(503, errorhandlers.internal)

    return app
