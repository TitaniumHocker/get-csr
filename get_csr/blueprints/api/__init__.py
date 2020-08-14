# -*- coding: utf-8 -*-
import re

from flask import Blueprint, request, make_response, jsonify
from webargs import fields, validate
from webargs.flaskparser import use_args
from get_csr.csr import CSRGenerator


api = Blueprint('api', __name__)

country_regexp = re.compile(r'^([A-Z]{2})$')
alt_names_regexp = re.compile(r'^([A-Za-z\*\.]+)(,(\ )?[A-Za-z\*\.]+)*$')

csr_args = {
    'country': fields.Str(required=True, validate=lambda c: country_regexp.match(c)),
    'state': fields.Str(required=True),
    'locality': fields.Str(required=True),
    'organization': fields.Str(required=True),
    'org_unit': fields.Str(required=False),
    'common_name': fields.Str(required=True),
    'alt_names': fields.Str(required=False, validate=lambda a: alt_names_regexp.match(a)),
    'key_size': fields.Integer(required=True, validate=validate.OneOf((1024, 2048, 4096,)))
}

@api.route('/generate', methods=['POST'])
@use_args(csr_args, location='json')
def gen(args):
    generator = CSRGenerator(
        country=args['country'],
        state=args['state'],
        locality=args['locality'],
        organization=args['organization'],
        common_name=args['common_name'],
        alternative_names=args['alt_names'],
        key_size=args['key_size']
    )

    return make_response(
        jsonify({'CSR': generator.csr_pem, 'Private Key': generator.pk_pem}), 200
    )
