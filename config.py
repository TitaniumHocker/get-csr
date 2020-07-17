# -*- coding: utf-8 -*-


class BasicConfig:
    '''Basic configuration object'''


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
