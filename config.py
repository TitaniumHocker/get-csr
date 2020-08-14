# -*- coding: utf-8 -*-
from os import environ

class BasicConfig:
    '''Basic configuration object'''
    LANGUAGES = ['en', 'ru']
    SECRET_KEY = environ.get('SECRET_KEY')


class DevelopmentConfig(BasicConfig):
    '''Development configuration object'''
    DEBUG = True


class TestingConfig(DevelopmentConfig):
    '''Testing configuration object'''
    TESTING = True


class ProductionConfig(BasicConfig):
    '''Production configuration object'''


configurations = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
