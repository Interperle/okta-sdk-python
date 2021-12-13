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

class SamlAttributeStatement(object):
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
        'name': 'str',
        'namespace': 'str',
        'type': 'str',
        'filter_type': 'str',
        'filter_value': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'type': 'type',
        'filter_type': 'filterType',
        'filter_value': 'filterValue',
        'values': 'values'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, name=None, namespace=None, type=None, filter_type=None, filter_value=None, values=None):  # noqa: E501
        """SamlAttributeStatement - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._namespace = None
        self._type = None
        self._filter_type = None
        self._filter_value = None
        self._values = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if type is not None:
            self.type = type
        if filter_type is not None:
            self.filter_type = filter_type
        if filter_value is not None:
            self.filter_value = filter_value
        if values is not None:
            self.values = values

    @property
    def name(self):
        """Gets the name of this SamlAttributeStatement.  # noqa: E501


        :return: The name of this SamlAttributeStatement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SamlAttributeStatement.


        :param name: The name of this SamlAttributeStatement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this SamlAttributeStatement.  # noqa: E501


        :return: The namespace of this SamlAttributeStatement.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this SamlAttributeStatement.


        :param namespace: The namespace of this SamlAttributeStatement.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def type(self):
        """Gets the type of this SamlAttributeStatement.  # noqa: E501


        :return: The type of this SamlAttributeStatement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SamlAttributeStatement.


        :param type: The type of this SamlAttributeStatement.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def filter_type(self):
        """Gets the filter_type of this SamlAttributeStatement.  # noqa: E501


        :return: The filter_type of this SamlAttributeStatement.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this SamlAttributeStatement.


        :param filter_type: The filter_type of this SamlAttributeStatement.  # noqa: E501
        :type: str
        """

        self._filter_type = filter_type

    @property
    def filter_value(self):
        """Gets the filter_value of this SamlAttributeStatement.  # noqa: E501


        :return: The filter_value of this SamlAttributeStatement.  # noqa: E501
        :rtype: str
        """
        return self._filter_value

    @filter_value.setter
    def filter_value(self, filter_value):
        """Sets the filter_value of this SamlAttributeStatement.


        :param filter_value: The filter_value of this SamlAttributeStatement.  # noqa: E501
        :type: str
        """

        self._filter_value = filter_value

    @property
    def values(self):
        """Gets the values of this SamlAttributeStatement.  # noqa: E501


        :return: The values of this SamlAttributeStatement.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this SamlAttributeStatement.


        :param values: The values of this SamlAttributeStatement.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if issubclass(SamlAttributeStatement, dict):
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
        if not isinstance(other, SamlAttributeStatement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
