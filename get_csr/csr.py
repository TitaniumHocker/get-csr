# -*- coding: utf-8 -*-
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from cryptography import x509


class CSRGenerator:
    '''Thing to create Certificate Signing Request

    Simple class with simple interface for creating CSR

    :param country: two letter abbreviation of country
    :param state: full state name
    :param locality: full city name
    :param organization: company name or personal name
    :param common_name: the fully qualified domain name
    :param organizational_unit: company department, optional
    :param alternative_names: alternative domain names, optional'''
    def __init__(
            self,
            country: str,
            state: str,
            locality: str,
            organization: str,
            common_name: str,
            organizational_unit: str = None,
            alternative_names: list = [],
            key_size: int = 2048
    ):
        self.cn = common_name
        self.pkey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        self.name_atributes = [
            x509.NameAttribute(NameOID.COUNTRY_NAME, country),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
            x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
        ]
        if organizational_unit:
            self.name_atributes.append(
                x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, organizational_unit)
            )

        self.alt_names = [
            x509.DNSName(name) for name in set([common_name, *alternative_names])
        ]

        self.csr = x509.CertificateSigningRequestBuilder().subject_name(
            x509.Name(self.name_atributes)
        ).add_extension(
            x509.SubjectAlternativeName(self.alt_names), critical=False
        ).sign(self.pkey, hashes.SHA256(), default_backend())

    def __str__(self):
        return 'CSRGenerator for {}'.format(self.cn)

    def __repr__(self):
        return '<CSRGenerator {}>'.format(self.cn)

    @property
    def pk_pem(self) -> str:
        """str: private key in PEM format"""
        return self.pkey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')

    @property
    def csr_pem(self) -> str:
        """str: csr in PEM format"""
        return self.csr.public_bytes(serialization.Encoding.PEM).decode('utf-8')
