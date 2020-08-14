# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from flask_babelex import lazy_gettext as _l
from get_csr.blueprints.public.forms import CSRForm
from get_csr.blueprints.public import public
from get_csr.csr import CSRGenerator
from pdb import set_trace


@public.route('/', methods=['GET', 'POST'])
def index():
    csr_form = CSRForm()
    if csr_form.validate_on_submit():
        generator = CSRGenerator(
            country=csr_form.country.data,
            state=csr_form.state.data,
            locality=csr_form.locality.data,
            organization=csr_form.organization.data,
            organizational_unit=csr_form.org_unit.data,
            common_name=csr_form.common_name.data,
            alternative_names=[name.strip() for name in csr_form.alt_names.data.split(',')],
            key_size=int(csr_form.key_size.data)
        )
        return render_template('success.jinja.html', csr=generator.csr_pem, pk=generator.pk_pem)
    return render_template('index.jinja.html', form=csr_form)


@public.route('/readme')
def readme():
    return render_template('readme.jinja.html', ptitle=_l('Info'))


@public.route('/api-docs')
def api_docs():
    return render_template('api_doc.jinja.html', ptitle=_l('API'))
