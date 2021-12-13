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

class OAuth2Scope(object):
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
        'consent': 'str',
        'default': 'bool',
        'description': 'str',
        'display_name': 'str',
        'id': 'str',
        'metadata_publish': 'str',
        'name': 'str',
        'system': 'bool'
    }

    attribute_map = {
        'consent': 'consent',
        'default': 'default',
        'description': 'description',
        'display_name': 'displayName',
        'id': 'id',
        'metadata_publish': 'metadataPublish',
        'name': 'name',
        'system': 'system'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, consent=None, default=None, description=None, display_name=None, id=None, metadata_publish=None, name=None, system=None):  # noqa: E501
        """OAuth2Scope - a model defined in Swagger"""  # noqa: E501
        self._consent = None
        self._default = None
        self._description = None
        self._display_name = None
        self._id = None
        self._metadata_publish = None
        self._name = None
        self._system = None
        self.discriminator = None
        if consent is not None:
            self.consent = consent
        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if metadata_publish is not None:
            self.metadata_publish = metadata_publish
        if name is not None:
            self.name = name
        if system is not None:
            self.system = system

    @property
    def consent(self):
        """Gets the consent of this OAuth2Scope.  # noqa: E501


        :return: The consent of this OAuth2Scope.  # noqa: E501
        :rtype: str
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this OAuth2Scope.


        :param consent: The consent of this OAuth2Scope.  # noqa: E501
        :type: str
        """
        allowed_values = ["REQUIRED", "IMPLICIT", "ADMIN"]  # noqa: E501
        if consent not in allowed_values:
            raise ValueError(
                "Invalid value for `consent` ({0}), must be one of {1}"  # noqa: E501
                .format(consent, allowed_values)
            )

        self._consent = consent

    @property
    def default(self):
        """Gets the default of this OAuth2Scope.  # noqa: E501


        :return: The default of this OAuth2Scope.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this OAuth2Scope.


        :param default: The default of this OAuth2Scope.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this OAuth2Scope.  # noqa: E501


        :return: The description of this OAuth2Scope.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OAuth2Scope.


        :param description: The description of this OAuth2Scope.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this OAuth2Scope.  # noqa: E501


        :return: The display_name of this OAuth2Scope.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this OAuth2Scope.


        :param display_name: The display_name of this OAuth2Scope.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this OAuth2Scope.  # noqa: E501


        :return: The id of this OAuth2Scope.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OAuth2Scope.


        :param id: The id of this OAuth2Scope.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def metadata_publish(self):
        """Gets the metadata_publish of this OAuth2Scope.  # noqa: E501


        :return: The metadata_publish of this OAuth2Scope.  # noqa: E501
        :rtype: str
        """
        return self._metadata_publish

    @metadata_publish.setter
    def metadata_publish(self, metadata_publish):
        """Sets the metadata_publish of this OAuth2Scope.


        :param metadata_publish: The metadata_publish of this OAuth2Scope.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALL_CLIENTS", "NO_CLIENTS"]  # noqa: E501
        if metadata_publish not in allowed_values:
            raise ValueError(
                "Invalid value for `metadata_publish` ({0}), must be one of {1}"  # noqa: E501
                .format(metadata_publish, allowed_values)
            )

        self._metadata_publish = metadata_publish

    @property
    def name(self):
        """Gets the name of this OAuth2Scope.  # noqa: E501


        :return: The name of this OAuth2Scope.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OAuth2Scope.


        :param name: The name of this OAuth2Scope.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def system(self):
        """Gets the system of this OAuth2Scope.  # noqa: E501


        :return: The system of this OAuth2Scope.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this OAuth2Scope.


        :param system: The system of this OAuth2Scope.  # noqa: E501
        :type: bool
        """

        self._system = system

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
        if issubclass(OAuth2Scope, dict):
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
        if not isinstance(other, OAuth2Scope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
