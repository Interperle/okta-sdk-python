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

class PolicyRuleAuthContextCondition(object):
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
        'auth_type': 'str'
    }

    attribute_map = {
        'auth_type': 'authType'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, auth_type=None):  # noqa: E501
        """PolicyRuleAuthContextCondition - a model defined in Swagger"""  # noqa: E501
        self._auth_type = None
        self.discriminator = None
        if auth_type is not None:
            self.auth_type = auth_type

    @property
    def auth_type(self):
        """Gets the auth_type of this PolicyRuleAuthContextCondition.  # noqa: E501


        :return: The auth_type of this PolicyRuleAuthContextCondition.  # noqa: E501
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this PolicyRuleAuthContextCondition.


        :param auth_type: The auth_type of this PolicyRuleAuthContextCondition.  # noqa: E501
        :type: str
        """
        allowed_values = ["ANY", "RADIUS"]  # noqa: E501
        if auth_type not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_type` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_type, allowed_values)
            )

        self._auth_type = auth_type

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
        if issubclass(PolicyRuleAuthContextCondition, dict):
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
        if not isinstance(other, PolicyRuleAuthContextCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
