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

class SamlApplicationSettingsSignOn(object):
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
        'allow_multiple_acs_endpoints': 'bool',
        'acs_endpoints': 'list[AcsEndpoint]',
        'assertion_signed': 'bool',
        'attribute_statements': 'list[SamlAttributeStatement]',
        'audience': 'str',
        'audience_override': 'str',
        'authn_context_class_ref': 'str',
        'default_relay_state': 'str',
        'destination': 'str',
        'destination_override': 'str',
        'digest_algorithm': 'str',
        'honor_force_authn': 'bool',
        'idp_issuer': 'str',
        'inline_hooks': 'list[SignOnInlineHook]',
        'recipient': 'str',
        'recipient_override': 'str',
        'request_compressed': 'bool',
        'response_signed': 'bool',
        'signature_algorithm': 'str',
        'slo': 'SingleLogout',
        'sp_issuer': 'str',
        'sso_acs_url': 'str',
        'sso_acs_url_override': 'str',
        'sp_certificate': 'SpCertificate',
        'subject_name_id_format': 'str',
        'subject_name_id_template': 'str'
    }

    attribute_map = {
        'allow_multiple_acs_endpoints': 'allowMultipleAcsEndpoints',
        'acs_endpoints': 'acsEndpoints',
        'assertion_signed': 'assertionSigned',
        'attribute_statements': 'attributeStatements',
        'audience': 'audience',
        'audience_override': 'audienceOverride',
        'authn_context_class_ref': 'authnContextClassRef',
        'default_relay_state': 'defaultRelayState',
        'destination': 'destination',
        'destination_override': 'destinationOverride',
        'digest_algorithm': 'digestAlgorithm',
        'honor_force_authn': 'honorForceAuthn',
        'idp_issuer': 'idpIssuer',
        'inline_hooks': 'inlineHooks',
        'recipient': 'recipient',
        'recipient_override': 'recipientOverride',
        'request_compressed': 'requestCompressed',
        'response_signed': 'responseSigned',
        'signature_algorithm': 'signatureAlgorithm',
        'slo': 'slo',
        'sp_issuer': 'spIssuer',
        'sso_acs_url': 'ssoAcsUrl',
        'sso_acs_url_override': 'ssoAcsUrlOverride',
        'sp_certificate': 'spCertificate',
        'subject_name_id_format': 'subjectNameIdFormat',
        'subject_name_id_template': 'subjectNameIdTemplate'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, allow_multiple_acs_endpoints=None, acs_endpoints=None, assertion_signed=None, attribute_statements=None, audience=None, audience_override=None, authn_context_class_ref=None, default_relay_state=None, destination=None, destination_override=None, digest_algorithm=None, honor_force_authn=None, idp_issuer=None, inline_hooks=None, recipient=None, recipient_override=None, request_compressed=None, response_signed=None, signature_algorithm=None, slo=None, sp_issuer=None, sso_acs_url=None, sso_acs_url_override=None, sp_certificate=None, subject_name_id_format=None, subject_name_id_template=None):  # noqa: E501
        """SamlApplicationSettingsSignOn - a model defined in Swagger"""  # noqa: E501
        self._allow_multiple_acs_endpoints = None
        self._acs_endpoints = None
        self._assertion_signed = None
        self._attribute_statements = None
        self._audience = None
        self._audience_override = None
        self._authn_context_class_ref = None
        self._default_relay_state = None
        self._destination = None
        self._destination_override = None
        self._digest_algorithm = None
        self._honor_force_authn = None
        self._idp_issuer = None
        self._inline_hooks = None
        self._recipient = None
        self._recipient_override = None
        self._request_compressed = None
        self._response_signed = None
        self._signature_algorithm = None
        self._slo = None
        self._sp_issuer = None
        self._sso_acs_url = None
        self._sso_acs_url_override = None
        self._sp_certificate = None
        self._subject_name_id_format = None
        self._subject_name_id_template = None
        self.discriminator = None
        if allow_multiple_acs_endpoints is not None:
            self.allow_multiple_acs_endpoints = allow_multiple_acs_endpoints
        if acs_endpoints is not None:
            self.acs_endpoints = acs_endpoints
        if assertion_signed is not None:
            self.assertion_signed = assertion_signed
        if attribute_statements is not None:
            self.attribute_statements = attribute_statements
        if audience is not None:
            self.audience = audience
        if audience_override is not None:
            self.audience_override = audience_override
        if authn_context_class_ref is not None:
            self.authn_context_class_ref = authn_context_class_ref
        if default_relay_state is not None:
            self.default_relay_state = default_relay_state
        if destination is not None:
            self.destination = destination
        if destination_override is not None:
            self.destination_override = destination_override
        if digest_algorithm is not None:
            self.digest_algorithm = digest_algorithm
        if honor_force_authn is not None:
            self.honor_force_authn = honor_force_authn
        if idp_issuer is not None:
            self.idp_issuer = idp_issuer
        if inline_hooks is not None:
            self.inline_hooks = inline_hooks
        if recipient is not None:
            self.recipient = recipient
        if recipient_override is not None:
            self.recipient_override = recipient_override
        if request_compressed is not None:
            self.request_compressed = request_compressed
        if response_signed is not None:
            self.response_signed = response_signed
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if slo is not None:
            self.slo = slo
        if sp_issuer is not None:
            self.sp_issuer = sp_issuer
        if sso_acs_url is not None:
            self.sso_acs_url = sso_acs_url
        if sso_acs_url_override is not None:
            self.sso_acs_url_override = sso_acs_url_override
        if sp_certificate is not None:
            self.sp_certificate = sp_certificate
        if subject_name_id_format is not None:
            self.subject_name_id_format = subject_name_id_format
        if subject_name_id_template is not None:
            self.subject_name_id_template = subject_name_id_template

    @property
    def allow_multiple_acs_endpoints(self):
        """Gets the allow_multiple_acs_endpoints of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The allow_multiple_acs_endpoints of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multiple_acs_endpoints

    @allow_multiple_acs_endpoints.setter
    def allow_multiple_acs_endpoints(self, allow_multiple_acs_endpoints):
        """Sets the allow_multiple_acs_endpoints of this SamlApplicationSettingsSignOn.


        :param allow_multiple_acs_endpoints: The allow_multiple_acs_endpoints of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: bool
        """

        self._allow_multiple_acs_endpoints = allow_multiple_acs_endpoints

    @property
    def acs_endpoints(self):
        """Gets the acs_endpoints of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The acs_endpoints of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: list[AcsEndpoint]
        """
        return self._acs_endpoints

    @acs_endpoints.setter
    def acs_endpoints(self, acs_endpoints):
        """Sets the acs_endpoints of this SamlApplicationSettingsSignOn.


        :param acs_endpoints: The acs_endpoints of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: list[AcsEndpoint]
        """

        self._acs_endpoints = acs_endpoints

    @property
    def assertion_signed(self):
        """Gets the assertion_signed of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The assertion_signed of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: bool
        """
        return self._assertion_signed

    @assertion_signed.setter
    def assertion_signed(self, assertion_signed):
        """Sets the assertion_signed of this SamlApplicationSettingsSignOn.


        :param assertion_signed: The assertion_signed of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: bool
        """

        self._assertion_signed = assertion_signed

    @property
    def attribute_statements(self):
        """Gets the attribute_statements of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The attribute_statements of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: list[SamlAttributeStatement]
        """
        return self._attribute_statements

    @attribute_statements.setter
    def attribute_statements(self, attribute_statements):
        """Sets the attribute_statements of this SamlApplicationSettingsSignOn.


        :param attribute_statements: The attribute_statements of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: list[SamlAttributeStatement]
        """

        self._attribute_statements = attribute_statements

    @property
    def audience(self):
        """Gets the audience of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The audience of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this SamlApplicationSettingsSignOn.


        :param audience: The audience of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._audience = audience

    @property
    def audience_override(self):
        """Gets the audience_override of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The audience_override of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._audience_override

    @audience_override.setter
    def audience_override(self, audience_override):
        """Sets the audience_override of this SamlApplicationSettingsSignOn.


        :param audience_override: The audience_override of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._audience_override = audience_override

    @property
    def authn_context_class_ref(self):
        """Gets the authn_context_class_ref of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The authn_context_class_ref of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._authn_context_class_ref

    @authn_context_class_ref.setter
    def authn_context_class_ref(self, authn_context_class_ref):
        """Sets the authn_context_class_ref of this SamlApplicationSettingsSignOn.


        :param authn_context_class_ref: The authn_context_class_ref of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._authn_context_class_ref = authn_context_class_ref

    @property
    def default_relay_state(self):
        """Gets the default_relay_state of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The default_relay_state of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._default_relay_state

    @default_relay_state.setter
    def default_relay_state(self, default_relay_state):
        """Sets the default_relay_state of this SamlApplicationSettingsSignOn.


        :param default_relay_state: The default_relay_state of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._default_relay_state = default_relay_state

    @property
    def destination(self):
        """Gets the destination of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The destination of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this SamlApplicationSettingsSignOn.


        :param destination: The destination of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def destination_override(self):
        """Gets the destination_override of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The destination_override of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._destination_override

    @destination_override.setter
    def destination_override(self, destination_override):
        """Sets the destination_override of this SamlApplicationSettingsSignOn.


        :param destination_override: The destination_override of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._destination_override = destination_override

    @property
    def digest_algorithm(self):
        """Gets the digest_algorithm of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The digest_algorithm of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._digest_algorithm

    @digest_algorithm.setter
    def digest_algorithm(self, digest_algorithm):
        """Sets the digest_algorithm of this SamlApplicationSettingsSignOn.


        :param digest_algorithm: The digest_algorithm of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._digest_algorithm = digest_algorithm

    @property
    def honor_force_authn(self):
        """Gets the honor_force_authn of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The honor_force_authn of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: bool
        """
        return self._honor_force_authn

    @honor_force_authn.setter
    def honor_force_authn(self, honor_force_authn):
        """Sets the honor_force_authn of this SamlApplicationSettingsSignOn.


        :param honor_force_authn: The honor_force_authn of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: bool
        """

        self._honor_force_authn = honor_force_authn

    @property
    def idp_issuer(self):
        """Gets the idp_issuer of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The idp_issuer of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._idp_issuer

    @idp_issuer.setter
    def idp_issuer(self, idp_issuer):
        """Sets the idp_issuer of this SamlApplicationSettingsSignOn.


        :param idp_issuer: The idp_issuer of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._idp_issuer = idp_issuer

    @property
    def inline_hooks(self):
        """Gets the inline_hooks of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The inline_hooks of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: list[SignOnInlineHook]
        """
        return self._inline_hooks

    @inline_hooks.setter
    def inline_hooks(self, inline_hooks):
        """Sets the inline_hooks of this SamlApplicationSettingsSignOn.


        :param inline_hooks: The inline_hooks of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: list[SignOnInlineHook]
        """

        self._inline_hooks = inline_hooks

    @property
    def recipient(self):
        """Gets the recipient of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The recipient of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this SamlApplicationSettingsSignOn.


        :param recipient: The recipient of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._recipient = recipient

    @property
    def recipient_override(self):
        """Gets the recipient_override of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The recipient_override of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._recipient_override

    @recipient_override.setter
    def recipient_override(self, recipient_override):
        """Sets the recipient_override of this SamlApplicationSettingsSignOn.


        :param recipient_override: The recipient_override of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._recipient_override = recipient_override

    @property
    def request_compressed(self):
        """Gets the request_compressed of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The request_compressed of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: bool
        """
        return self._request_compressed

    @request_compressed.setter
    def request_compressed(self, request_compressed):
        """Sets the request_compressed of this SamlApplicationSettingsSignOn.


        :param request_compressed: The request_compressed of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: bool
        """

        self._request_compressed = request_compressed

    @property
    def response_signed(self):
        """Gets the response_signed of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The response_signed of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: bool
        """
        return self._response_signed

    @response_signed.setter
    def response_signed(self, response_signed):
        """Sets the response_signed of this SamlApplicationSettingsSignOn.


        :param response_signed: The response_signed of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: bool
        """

        self._response_signed = response_signed

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The signature_algorithm of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this SamlApplicationSettingsSignOn.


        :param signature_algorithm: The signature_algorithm of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._signature_algorithm = signature_algorithm

    @property
    def slo(self):
        """Gets the slo of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The slo of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: SingleLogout
        """
        return self._slo

    @slo.setter
    def slo(self, slo):
        """Sets the slo of this SamlApplicationSettingsSignOn.


        :param slo: The slo of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: SingleLogout
        """

        self._slo = slo

    @property
    def sp_issuer(self):
        """Gets the sp_issuer of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The sp_issuer of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._sp_issuer

    @sp_issuer.setter
    def sp_issuer(self, sp_issuer):
        """Sets the sp_issuer of this SamlApplicationSettingsSignOn.


        :param sp_issuer: The sp_issuer of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._sp_issuer = sp_issuer

    @property
    def sso_acs_url(self):
        """Gets the sso_acs_url of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The sso_acs_url of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._sso_acs_url

    @sso_acs_url.setter
    def sso_acs_url(self, sso_acs_url):
        """Sets the sso_acs_url of this SamlApplicationSettingsSignOn.


        :param sso_acs_url: The sso_acs_url of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._sso_acs_url = sso_acs_url

    @property
    def sso_acs_url_override(self):
        """Gets the sso_acs_url_override of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The sso_acs_url_override of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._sso_acs_url_override

    @sso_acs_url_override.setter
    def sso_acs_url_override(self, sso_acs_url_override):
        """Sets the sso_acs_url_override of this SamlApplicationSettingsSignOn.


        :param sso_acs_url_override: The sso_acs_url_override of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._sso_acs_url_override = sso_acs_url_override

    @property
    def sp_certificate(self):
        """Gets the sp_certificate of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The sp_certificate of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: SpCertificate
        """
        return self._sp_certificate

    @sp_certificate.setter
    def sp_certificate(self, sp_certificate):
        """Sets the sp_certificate of this SamlApplicationSettingsSignOn.


        :param sp_certificate: The sp_certificate of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: SpCertificate
        """

        self._sp_certificate = sp_certificate

    @property
    def subject_name_id_format(self):
        """Gets the subject_name_id_format of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The subject_name_id_format of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._subject_name_id_format

    @subject_name_id_format.setter
    def subject_name_id_format(self, subject_name_id_format):
        """Sets the subject_name_id_format of this SamlApplicationSettingsSignOn.


        :param subject_name_id_format: The subject_name_id_format of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._subject_name_id_format = subject_name_id_format

    @property
    def subject_name_id_template(self):
        """Gets the subject_name_id_template of this SamlApplicationSettingsSignOn.  # noqa: E501


        :return: The subject_name_id_template of this SamlApplicationSettingsSignOn.  # noqa: E501
        :rtype: str
        """
        return self._subject_name_id_template

    @subject_name_id_template.setter
    def subject_name_id_template(self, subject_name_id_template):
        """Sets the subject_name_id_template of this SamlApplicationSettingsSignOn.


        :param subject_name_id_template: The subject_name_id_template of this SamlApplicationSettingsSignOn.  # noqa: E501
        :type: str
        """

        self._subject_name_id_template = subject_name_id_template

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
        if issubclass(SamlApplicationSettingsSignOn, dict):
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
        if not isinstance(other, SamlApplicationSettingsSignOn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
