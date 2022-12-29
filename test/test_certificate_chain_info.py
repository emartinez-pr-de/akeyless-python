# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.certificate_chain_info import CertificateChainInfo  # noqa: E501
from akeyless.rest import ApiException

class TestCertificateChainInfo(unittest.TestCase):
    """CertificateChainInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CertificateChainInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.certificate_chain_info.CertificateChainInfo()  # noqa: E501
        if include_optional :
            return CertificateChainInfo(
                certificate_chain = [
                    akeyless.models.certificate_info.CertificateInfo(
                        ext_key_usage = [
                            56
                            ], 
                        key_usage = 56, 
                        dns_names = [
                            '0'
                            ], 
                        email_addresses = [
                            '0'
                            ], 
                        extensions = [
                            akeyless.models.extension.Extension(
                                critical = True, 
                                name = '0', 
                                value = '0', )
                            ], 
                        ip_addresses = [
                            '0'
                            ], 
                        is_ca = True, 
                        issuer = akeyless.models.name.Name(
                            country = [
                                '0'
                                ], 
                            extra_names = [
                                akeyless.models.attribute_type_and_value.AttributeTypeAndValue(
                                    type = [
                                        56
                                        ], 
                                    value = akeyless.models.value.Value(), )
                                ], 
                            locality = [
                                '0'
                                ], 
                            names = [
                                akeyless.models.attribute_type_and_value.AttributeTypeAndValue(
                                    type = [
                                        56
                                        ], 
                                    value = akeyless.models.value.Value(), )
                                ], 
                            serial_number = '0', 
                            street_address = [
                                '0'
                                ], ), 
                        issuing_certificate_url = [
                            '0'
                            ], 
                        key_size = 56, 
                        not_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        not_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        ocsp_server = [
                            '0'
                            ], 
                        public_key_algorithm_name = '0', 
                        serial_number = '0', 
                        sha_1_fingerprint = '0', 
                        sha_256_fingerprint = '0', 
                        signature = '0', 
                        signature_algorithm_name = '0', 
                        subject = akeyless.models.name.Name(
                            serial_number = '0', ), 
                        subject_public_key = '0', 
                        uris = [
                            '0'
                            ], 
                        version = 56, )
                    ], 
                certificate_pem = '0', 
                expiration_events = [
                    akeyless.models.certificate_expiration_event.CertificateExpirationEvent(
                        seconds_before = 56, )
                    ]
            )
        else :
            return CertificateChainInfo(
        )

    def testCertificateChainInfo(self):
        """Test CertificateChainInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
