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

class UserCredentials(object):
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
        'password': 'PasswordCredential',
        'provider': 'AuthenticationProvider',
        'recovery_question': 'RecoveryQuestionCredential'
    }

    attribute_map = {
        'password': 'password',
        'provider': 'provider',
        'recovery_question': 'recovery_question'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, password=None, provider=None, recovery_question=None):  # noqa: E501
        """UserCredentials - a model defined in Swagger"""  # noqa: E501
        self._password = None
        self._provider = None
        self._recovery_question = None
        self.discriminator = None
        if password is not None:
            self.password = password
        if provider is not None:
            self.provider = provider
        if recovery_question is not None:
            self.recovery_question = recovery_question

    @property
    def password(self):
        """Gets the password of this UserCredentials.  # noqa: E501


        :return: The password of this UserCredentials.  # noqa: E501
        :rtype: PasswordCredential
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserCredentials.


        :param password: The password of this UserCredentials.  # noqa: E501
        :type: PasswordCredential
        """

        self._password = password

    @property
    def provider(self):
        """Gets the provider of this UserCredentials.  # noqa: E501


        :return: The provider of this UserCredentials.  # noqa: E501
        :rtype: AuthenticationProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this UserCredentials.


        :param provider: The provider of this UserCredentials.  # noqa: E501
        :type: AuthenticationProvider
        """

        self._provider = provider

    @property
    def recovery_question(self):
        """Gets the recovery_question of this UserCredentials.  # noqa: E501


        :return: The recovery_question of this UserCredentials.  # noqa: E501
        :rtype: RecoveryQuestionCredential
        """
        return self._recovery_question

    @recovery_question.setter
    def recovery_question(self, recovery_question):
        """Sets the recovery_question of this UserCredentials.


        :param recovery_question: The recovery_question of this UserCredentials.  # noqa: E501
        :type: RecoveryQuestionCredential
        """

        self._recovery_question = recovery_question

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
        if issubclass(UserCredentials, dict):
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
        if not isinstance(other, UserCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
