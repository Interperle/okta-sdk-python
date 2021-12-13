# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserActivationToken(object):
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
        'activation_token': 'str',
        'activation_url': 'str'
    }

    attribute_map = {
        'activation_token': 'activationToken',
        'activation_url': 'activationUrl'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, activation_token=None, activation_url=None):  # noqa: E501
        """UserActivationToken - a model defined in Swagger"""  # noqa: E501
        self._activation_token = None
        self._activation_url = None
        self.discriminator = None
        if activation_token is not None:
            self.activation_token = activation_token
        if activation_url is not None:
            self.activation_url = activation_url

    @property
    def activation_token(self):
        """Gets the activation_token of this UserActivationToken.  # noqa: E501


        :return: The activation_token of this UserActivationToken.  # noqa: E501
        :rtype: str
        """
        return self._activation_token

    @activation_token.setter
    def activation_token(self, activation_token):
        """Sets the activation_token of this UserActivationToken.


        :param activation_token: The activation_token of this UserActivationToken.  # noqa: E501
        :type: str
        """

        self._activation_token = activation_token

    @property
    def activation_url(self):
        """Gets the activation_url of this UserActivationToken.  # noqa: E501


        :return: The activation_url of this UserActivationToken.  # noqa: E501
        :rtype: str
        """
        return self._activation_url

    @activation_url.setter
    def activation_url(self, activation_url):
        """Sets the activation_url of this UserActivationToken.


        :param activation_url: The activation_url of this UserActivationToken.  # noqa: E501
        :type: str
        """

        self._activation_url = activation_url

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
        if issubclass(UserActivationToken, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserActivationToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
