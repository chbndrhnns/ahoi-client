# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Account(object):
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
        'id': 'int',
        'name': 'str',
        'user_defined_name': 'str',
        'owner': 'str',
        'provider_id': 'int',
        'kind': 'str',
        'automatic_refresh_interval': 'int',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_defined_name': 'userDefinedName',
        'owner': 'owner',
        'provider_id': 'providerId',
        'kind': 'kind',
        'automatic_refresh_interval': 'automaticRefreshInterval',
        'type': 'type'
    }

    discriminator_value_class_map = {
        'BankAccount': 'BankAccount'
    }

    def __init__(self, id=None, name=None, user_defined_name=None, owner=None, provider_id=None, kind=None, automatic_refresh_interval=None, type=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._user_defined_name = None
        self._owner = None
        self._provider_id = None
        self._kind = None
        self._automatic_refresh_interval = None
        self._type = None
        self.discriminator = 'type'

        self.id = id
        self.name = name
        if user_defined_name is not None:
            self.user_defined_name = user_defined_name
        self.owner = owner
        self.provider_id = provider_id
        self.kind = kind
        self.automatic_refresh_interval = automatic_refresh_interval
        self.type = type

    @property
    def id(self):
        """Gets the id of this Account.  # noqa: E501

        Internal ID of this account (generated value)  # noqa: E501

        :return: The id of this Account.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.

        Internal ID of this account (generated value)  # noqa: E501

        :param id: The id of this Account.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501

        Account name returned by bank provider (e.g., \"Giro Account\")  # noqa: E501

        :return: The name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.

        Account name returned by bank provider (e.g., \"Giro Account\")  # noqa: E501

        :param name: The name of this Account.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def user_defined_name(self):
        """Gets the user_defined_name of this Account.  # noqa: E501

        Account userDefinedName. This value can be set to define a custom name used in AHOI (e.g., \"My Giro Account\").  Can be changed by using the account resource.  # noqa: E501

        :return: The user_defined_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._user_defined_name

    @user_defined_name.setter
    def user_defined_name(self, user_defined_name):
        """Sets the user_defined_name of this Account.

        Account userDefinedName. This value can be set to define a custom name used in AHOI (e.g., \"My Giro Account\").  Can be changed by using the account resource.  # noqa: E501

        :param user_defined_name: The user_defined_name of this Account.  # noqa: E501
        :type: str
        """

        self._user_defined_name = user_defined_name

    @property
    def owner(self):
        """Gets the owner of this Account.  # noqa: E501

        Account owner returned by bank provider (e.g., \"Max Mustermann\")  # noqa: E501

        :return: The owner of this Account.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Account.

        Account owner returned by bank provider (e.g., \"Max Mustermann\")  # noqa: E501

        :param owner: The owner of this Account.  # noqa: E501
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def provider_id(self):
        """Gets the provider_id of this Account.  # noqa: E501

        Identifier of the provider to which this account belongs  # noqa: E501

        :return: The provider_id of this Account.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this Account.

        Identifier of the provider to which this account belongs  # noqa: E501

        :param provider_id: The provider_id of this Account.  # noqa: E501
        :type: int
        """
        if provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def kind(self):
        """Gets the kind of this Account.  # noqa: E501

        An account kind is a classification of its structure and its possibilities.   This is typically defined by the bank provider.  # noqa: E501

        :return: The kind of this Account.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Account.

        An account kind is a classification of its structure and its possibilities.   This is typically defined by the bank provider.  # noqa: E501

        :param kind: The kind of this Account.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["GIRO", "SPAR", "FESTGELD", "DEPOT", "DARLEHEN", "KREDITKARTE", "BAUSPAR", "VL_SPAR", "VL_BAUSPAR", "VL_WERTPAPIERSPARVERTRAG", "XXX"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def automatic_refresh_interval(self):
        """Gets the automatic_refresh_interval of this Account.  # noqa: E501

        Interval that indicates the freguency of which the account is updated.   This interval is read-only and is determined by the server depending on created notifications and last use of the API. The range is between every hour, daily and monthly.  # noqa: E501

        :return: The automatic_refresh_interval of this Account.  # noqa: E501
        :rtype: int
        """
        return self._automatic_refresh_interval

    @automatic_refresh_interval.setter
    def automatic_refresh_interval(self, automatic_refresh_interval):
        """Sets the automatic_refresh_interval of this Account.

        Interval that indicates the freguency of which the account is updated.   This interval is read-only and is determined by the server depending on created notifications and last use of the API. The range is between every hour, daily and monthly.  # noqa: E501

        :param automatic_refresh_interval: The automatic_refresh_interval of this Account.  # noqa: E501
        :type: int
        """
        if automatic_refresh_interval is None:
            raise ValueError("Invalid value for `automatic_refresh_interval`, must not be `None`")  # noqa: E501

        self._automatic_refresh_interval = automatic_refresh_interval

    @property
    def type(self):
        """Gets the type of this Account.  # noqa: E501

        Discriminator for subtypes. At the moment only `BankAccount` is supported.  # noqa: E501

        :return: The type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Account.

        Discriminator for subtypes. At the moment only `BankAccount` is supported.  # noqa: E501

        :param type: The type of this Account.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other