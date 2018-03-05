# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NotificationTarget(object):
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
        'app_token': 'str',
        'product_id': 'str',
        'operating_system': 'str',
        'state': 'str',
        'locale': 'str'
    }

    attribute_map = {
        'id': 'id',
        'app_token': 'appToken',
        'product_id': 'productId',
        'operating_system': 'operatingSystem',
        'state': 'state',
        'locale': 'locale'
    }

    def __init__(self, id=None, app_token=None, product_id=None, operating_system=None, state=None, locale=None):  # noqa: E501
        """NotificationTarget - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._app_token = None
        self._product_id = None
        self._operating_system = None
        self._state = None
        self._locale = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.app_token = app_token
        self.product_id = product_id
        self.operating_system = operating_system
        if state is not None:
            self.state = state
        self.locale = locale

    @property
    def id(self):
        """Gets the id of this NotificationTarget.  # noqa: E501

        Internal ID of this notificationTarget (generated value)  # noqa: E501

        :return: The id of this NotificationTarget.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationTarget.

        Internal ID of this notificationTarget (generated value)  # noqa: E501

        :param id: The id of this NotificationTarget.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def app_token(self):
        """Gets the app_token of this NotificationTarget.  # noqa: E501

        Installation of specific application token to which to send push notifications. (e.g., device token on iOS devices)  # noqa: E501

        :return: The app_token of this NotificationTarget.  # noqa: E501
        :rtype: str
        """
        return self._app_token

    @app_token.setter
    def app_token(self, app_token):
        """Sets the app_token of this NotificationTarget.

        Installation of specific application token to which to send push notifications. (e.g., device token on iOS devices)  # noqa: E501

        :param app_token: The app_token of this NotificationTarget.  # noqa: E501
        :type: str
        """
        if app_token is None:
            raise ValueError("Invalid value for `app_token`, must not be `None`")  # noqa: E501

        self._app_token = app_token

    @property
    def product_id(self):
        """Gets the product_id of this NotificationTarget.  # noqa: E501

        ID of the application. Has to be set up in AHOI. Use \"sandbox-product\" in sandbox environment.  # noqa: E501

        :return: The product_id of this NotificationTarget.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this NotificationTarget.

        ID of the application. Has to be set up in AHOI. Use \"sandbox-product\" in sandbox environment.  # noqa: E501

        :param product_id: The product_id of this NotificationTarget.  # noqa: E501
        :type: str
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def operating_system(self):
        """Gets the operating_system of this NotificationTarget.  # noqa: E501

        Operating system of the application  # noqa: E501

        :return: The operating_system of this NotificationTarget.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this NotificationTarget.

        Operating system of the application  # noqa: E501

        :param operating_system: The operating_system of this NotificationTarget.  # noqa: E501
        :type: str
        """
        if operating_system is None:
            raise ValueError("Invalid value for `operating_system`, must not be `None`")  # noqa: E501
        allowed_values = ["IOS", "ANDROID"]  # noqa: E501
        if operating_system not in allowed_values:
            raise ValueError(
                "Invalid value for `operating_system` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system, allowed_values)
            )

        self._operating_system = operating_system

    @property
    def state(self):
        """Gets the state of this NotificationTarget.  # noqa: E501

        State of the application  # noqa: E501

        :return: The state of this NotificationTarget.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NotificationTarget.

        State of the application  # noqa: E501

        :param state: The state of this NotificationTarget.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "UNDEFINED", "TARGET_UNKNOWN", "INVALID_TOKEN_FORMAT"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def locale(self):
        """Gets the locale of this NotificationTarget.  # noqa: E501

        Locale used to determine notification titles and texts for this target.   Defaults to 'de_DE'.  # noqa: E501

        :return: The locale of this NotificationTarget.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this NotificationTarget.

        Locale used to determine notification titles and texts for this target.   Defaults to 'de_DE'.  # noqa: E501

        :param locale: The locale of this NotificationTarget.  # noqa: E501
        :type: str
        """
        if locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")  # noqa: E501

        self._locale = locale

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
        if not isinstance(other, NotificationTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other