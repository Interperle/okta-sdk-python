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

class SecurityQuestionUserFactorProfile(object):
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
        'answer': 'str',
        'question': 'str',
        'question_text': 'str'
    }

    attribute_map = {
        'answer': 'answer',
        'question': 'question',
        'question_text': 'questionText'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, answer=None, question=None, question_text=None):  # noqa: E501
        """SecurityQuestionUserFactorProfile - a model defined in Swagger"""  # noqa: E501
        self._answer = None
        self._question = None
        self._question_text = None
        self.discriminator = None
        if answer is not None:
            self.answer = answer
        if question is not None:
            self.question = question
        if question_text is not None:
            self.question_text = question_text

    @property
    def answer(self):
        """Gets the answer of this SecurityQuestionUserFactorProfile.  # noqa: E501


        :return: The answer of this SecurityQuestionUserFactorProfile.  # noqa: E501
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this SecurityQuestionUserFactorProfile.


        :param answer: The answer of this SecurityQuestionUserFactorProfile.  # noqa: E501
        :type: str
        """

        self._answer = answer

    @property
    def question(self):
        """Gets the question of this SecurityQuestionUserFactorProfile.  # noqa: E501


        :return: The question of this SecurityQuestionUserFactorProfile.  # noqa: E501
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this SecurityQuestionUserFactorProfile.


        :param question: The question of this SecurityQuestionUserFactorProfile.  # noqa: E501
        :type: str
        """

        self._question = question

    @property
    def question_text(self):
        """Gets the question_text of this SecurityQuestionUserFactorProfile.  # noqa: E501


        :return: The question_text of this SecurityQuestionUserFactorProfile.  # noqa: E501
        :rtype: str
        """
        return self._question_text

    @question_text.setter
    def question_text(self, question_text):
        """Sets the question_text of this SecurityQuestionUserFactorProfile.


        :param question_text: The question_text of this SecurityQuestionUserFactorProfile.  # noqa: E501
        :type: str
        """

        self._question_text = question_text

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
        if issubclass(SecurityQuestionUserFactorProfile, dict):
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
        if not isinstance(other, SecurityQuestionUserFactorProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
