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

class OrgContactTypeObj(object):
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
        'links': 'dict(str, object)',
        'contact_type': 'OrgContactType'
    }

    attribute_map = {
        'links': '_links',
        'contact_type': 'contactType'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, links=None, contact_type=None):  # noqa: E501
        """OrgContactTypeObj - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._contact_type = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if contact_type is not None:
            self.contact_type = contact_type

    @property
    def links(self):
        """Gets the links of this OrgContactTypeObj.  # noqa: E501


        :return: The links of this OrgContactTypeObj.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OrgContactTypeObj.


        :param links: The links of this OrgContactTypeObj.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def contact_type(self):
        """Gets the contact_type of this OrgContactTypeObj.  # noqa: E501


        :return: The contact_type of this OrgContactTypeObj.  # noqa: E501
        :rtype: OrgContactType
        """
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        """Sets the contact_type of this OrgContactTypeObj.


        :param contact_type: The contact_type of this OrgContactTypeObj.  # noqa: E501
        :type: OrgContactType
        """

        self._contact_type = contact_type

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
        if issubclass(OrgContactTypeObj, dict):
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
        if not isinstance(other, OrgContactTypeObj):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
