# -*- coding: utf-8 -*-
from flask_babelex import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Regexp


class CSRForm(FlaskForm):
    '''Form for creating CSR'''
    country = StringField(
        _l('Country'),
        validators=[
            DataRequired(),
            Regexp('[A-Z]{2}', message=_l('Must be 2 latin capital letters'))
        ],
        description=_l('Two letter abbreviation of country'),
        render_kw={'placeholder': 'US', 'maxlength': 2, 'pattern': '[A-Z]{2}'}
    )
    state = StringField(
        _l('State'), validators=[DataRequired()],
        description=_l('Full state name'),
        render_kw={'placeholder': 'Michigan'}
    )
    locality = StringField(
        _l('Locality'), validators=[DataRequired()],
        description=_l('Full city name'),
        render_kw={'placeholder': 'Detroit'}
    )
    organization = StringField(
        _l('Organization'), validators=[DataRequired()],
        description=_l('Company name or personal name'),
        render_kw={'placeholder': 'Horns and Hooves'}
    )
    org_unit = StringField(
        _l('Organizational Unit'), description=_l('Company department, optional'),
        render_kw={'placeholder': 'DevOps'}
    )
    common_name = StringField(
        _l('Common Name'), validators=[DataRequired()],
        description=_l('The fully qualified domain name'),
        render_kw={'placeholder': 'example.com'}
    )
    alt_names = StringField(
        _l('Alternative Names'), render_kw={'placeholder': 'example.net, *.example.com'},
        description=_l('Comma separated alternative domain names, optional')
    )
    key_size = RadioField(
        _l('Key Size'), validators=[DataRequired()],
        choices=(('1024', '1024'), ('2048', '2048'), ('4096', '4096')),
        description=_l('Size of the RSA modulus in bits'),
        default='2048'
    )
    submit = SubmitField(_l('Generate CSR'))
