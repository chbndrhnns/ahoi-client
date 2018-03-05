# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.balance import Balance  # noqa: F401,E501
from swagger_client.models.forecast import Forecast  # noqa: F401,E501
from swagger_client.models.transaction import Transaction  # noqa: F401,E501


class ForecastTransaction(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'forecast_balance': 'Balance',
        'account_id': 'int',
        'transactions': 'list[Transaction]'
    }

    attribute_map = {
        'forecast_balance': 'forecastBalance',
        'account_id': 'accountId',
        'transactions': 'transactions'
    }

    def __init__(self, forecast_balance=None, account_id=None, transactions=None):  # noqa: E501
        """ForecastTransaction - a model defined in Swagger"""  # noqa: E501

        self._forecast_balance = None
        self._account_id = None
        self._transactions = None
        self.discriminator = None

        self.forecast_balance = forecast_balance
        self.account_id = account_id
        self.transactions = transactions

    @property
    def forecast_balance(self):
        """Gets the forecast_balance of this ForecastTransaction.  # noqa: E501

        Balance forecast  # noqa: E501

        :return: The forecast_balance of this ForecastTransaction.  # noqa: E501
        :rtype: Balance
        """
        return self._forecast_balance

    @forecast_balance.setter
    def forecast_balance(self, forecast_balance):
        """Sets the forecast_balance of this ForecastTransaction.

        Balance forecast  # noqa: E501

        :param forecast_balance: The forecast_balance of this ForecastTransaction.  # noqa: E501
        :type: Balance
        """
        if forecast_balance is None:
            raise ValueError("Invalid value for `forecast_balance`, must not be `None`")  # noqa: E501

        self._forecast_balance = forecast_balance

    @property
    def account_id(self):
        """Gets the account_id of this ForecastTransaction.  # noqa: E501

        Id of account this entry belongs to  # noqa: E501

        :return: The account_id of this ForecastTransaction.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ForecastTransaction.

        Id of account this entry belongs to  # noqa: E501

        :param account_id: The account_id of this ForecastTransaction.  # noqa: E501
        :type: int
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def transactions(self):
        """Gets the transactions of this ForecastTransaction.  # noqa: E501

        List of unappliedTransaction  # noqa: E501

        :return: The transactions of this ForecastTransaction.  # noqa: E501
        :rtype: list[Transaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this ForecastTransaction.

        List of unappliedTransaction  # noqa: E501

        :param transactions: The transactions of this ForecastTransaction.  # noqa: E501
        :type: list[Transaction]
        """
        if transactions is None:
            raise ValueError("Invalid value for `transactions`, must not be `None`")  # noqa: E501

        self._transactions = transactions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ForecastTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other