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

class LogActor(object):
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
        'alternate_id': 'str',
        'detail': 'dict(str, object)',
        'display_name': 'str',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'alternate_id': 'alternateId',
        'detail': 'detail',
        'display_name': 'displayName',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, alternate_id=None, detail=None, display_name=None, id=None, type=None):  # noqa: E501
        """LogActor - a model defined in Swagger"""  # noqa: E501
        self._alternate_id = None
        self._detail = None
        self._display_name = None
        self._id = None
        self._type = None
        self.discriminator = None
        if alternate_id is not None:
            self.alternate_id = alternate_id
        if detail is not None:
            self.detail = detail
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def alternate_id(self):
        """Gets the alternate_id of this LogActor.  # noqa: E501


        :return: The alternate_id of this LogActor.  # noqa: E501
        :rtype: str
        """
        return self._alternate_id

    @alternate_id.setter
    def alternate_id(self, alternate_id):
        """Sets the alternate_id of this LogActor.


        :param alternate_id: The alternate_id of this LogActor.  # noqa: E501
        :type: str
        """

        self._alternate_id = alternate_id

    @property
    def detail(self):
        """Gets the detail of this LogActor.  # noqa: E501


        :return: The detail of this LogActor.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this LogActor.


        :param detail: The detail of this LogActor.  # noqa: E501
        :type: dict(str, object)
        """

        self._detail = detail

    @property
    def display_name(self):
        """Gets the display_name of this LogActor.  # noqa: E501


        :return: The display_name of this LogActor.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this LogActor.


        :param display_name: The display_name of this LogActor.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this LogActor.  # noqa: E501


        :return: The id of this LogActor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogActor.


        :param id: The id of this LogActor.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this LogActor.  # noqa: E501


        :return: The type of this LogActor.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LogActor.


        :param type: The type of this LogActor.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(LogActor, dict):
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
        if not isinstance(other, LogActor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
