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

class EventHookChannelConfig(object):
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
        'auth_scheme': 'EventHookChannelConfigAuthScheme',
        'headers': 'list[EventHookChannelConfigHeader]',
        'uri': 'str'
    }

    attribute_map = {
        'auth_scheme': 'authScheme',
        'headers': 'headers',
        'uri': 'uri'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, auth_scheme=None, headers=None, uri=None):  # noqa: E501
        """EventHookChannelConfig - a model defined in Swagger"""  # noqa: E501
        self._auth_scheme = None
        self._headers = None
        self._uri = None
        self.discriminator = None
        if auth_scheme is not None:
            self.auth_scheme = auth_scheme
        if headers is not None:
            self.headers = headers
        if uri is not None:
            self.uri = uri

    @property
    def auth_scheme(self):
        """Gets the auth_scheme of this EventHookChannelConfig.  # noqa: E501


        :return: The auth_scheme of this EventHookChannelConfig.  # noqa: E501
        :rtype: EventHookChannelConfigAuthScheme
        """
        return self._auth_scheme

    @auth_scheme.setter
    def auth_scheme(self, auth_scheme):
        """Sets the auth_scheme of this EventHookChannelConfig.


        :param auth_scheme: The auth_scheme of this EventHookChannelConfig.  # noqa: E501
        :type: EventHookChannelConfigAuthScheme
        """

        self._auth_scheme = auth_scheme

    @property
    def headers(self):
        """Gets the headers of this EventHookChannelConfig.  # noqa: E501


        :return: The headers of this EventHookChannelConfig.  # noqa: E501
        :rtype: list[EventHookChannelConfigHeader]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this EventHookChannelConfig.


        :param headers: The headers of this EventHookChannelConfig.  # noqa: E501
        :type: list[EventHookChannelConfigHeader]
        """

        self._headers = headers

    @property
    def uri(self):
        """Gets the uri of this EventHookChannelConfig.  # noqa: E501


        :return: The uri of this EventHookChannelConfig.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this EventHookChannelConfig.


        :param uri: The uri of this EventHookChannelConfig.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if issubclass(EventHookChannelConfig, dict):
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
        if not isinstance(other, EventHookChannelConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
