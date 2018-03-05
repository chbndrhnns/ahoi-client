# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.contracts_api import ContractsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestContractsApi(unittest.TestCase):
    """ContractsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.contracts_api.ContractsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_contract_list(self):
        """Test case for get_contract_list

        Retrieves the contract list for a given user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()