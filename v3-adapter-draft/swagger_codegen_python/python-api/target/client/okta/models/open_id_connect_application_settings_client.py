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

class OpenIdConnectApplicationSettingsClient(object):
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
        'application_type': 'OpenIdConnectApplicationType',
        'client_uri': 'str',
        'consent_method': 'OpenIdConnectApplicationConsentMethod',
        'grant_types': 'list[OAuthGrantType]',
        'initiate_login_uri': 'str',
        'issuer_mode': 'OpenIdConnectApplicationIssuerMode',
        'idp_initiated_login': 'OpenIdConnectApplicationIdpInitiatedLogin',
        'logo_uri': 'str',
        'policy_uri': 'str',
        'post_logout_redirect_uris': 'list[str]',
        'redirect_uris': 'list[str]',
        'wildcard_redirect': 'str',
        'response_types': 'list[OAuthResponseType]',
        'refresh_token': 'OpenIdConnectApplicationSettingsRefreshToken',
        'tos_uri': 'str',
        'jwks': 'OpenIdConnectApplicationSettingsClientKeys'
    }

    attribute_map = {
        'application_type': 'application_type',
        'client_uri': 'client_uri',
        'consent_method': 'consent_method',
        'grant_types': 'grant_types',
        'initiate_login_uri': 'initiate_login_uri',
        'issuer_mode': 'issuer_mode',
        'idp_initiated_login': 'idp_initiated_login',
        'logo_uri': 'logo_uri',
        'policy_uri': 'policy_uri',
        'post_logout_redirect_uris': 'post_logout_redirect_uris',
        'redirect_uris': 'redirect_uris',
        'wildcard_redirect': 'wildcard_redirect',
        'response_types': 'response_types',
        'refresh_token': 'refresh_token',
        'tos_uri': 'tos_uri',
        'jwks': 'jwks'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, application_type=None, client_uri=None, consent_method=None, grant_types=None, initiate_login_uri=None, issuer_mode=None, idp_initiated_login=None, logo_uri=None, policy_uri=None, post_logout_redirect_uris=None, redirect_uris=None, wildcard_redirect=None, response_types=None, refresh_token=None, tos_uri=None, jwks=None):  # noqa: E501
        """OpenIdConnectApplicationSettingsClient - a model defined in Swagger"""  # noqa: E501
        self._application_type = None
        self._client_uri = None
        self._consent_method = None
        self._grant_types = None
        self._initiate_login_uri = None
        self._issuer_mode = None
        self._idp_initiated_login = None
        self._logo_uri = None
        self._policy_uri = None
        self._post_logout_redirect_uris = None
        self._redirect_uris = None
        self._wildcard_redirect = None
        self._response_types = None
        self._refresh_token = None
        self._tos_uri = None
        self._jwks = None
        self.discriminator = None
        if application_type is not None:
            self.application_type = application_type
        if client_uri is not None:
            self.client_uri = client_uri
        if consent_method is not None:
            self.consent_method = consent_method
        if grant_types is not None:
            self.grant_types = grant_types
        if initiate_login_uri is not None:
            self.initiate_login_uri = initiate_login_uri
        if issuer_mode is not None:
            self.issuer_mode = issuer_mode
        if idp_initiated_login is not None:
            self.idp_initiated_login = idp_initiated_login
        if logo_uri is not None:
            self.logo_uri = logo_uri
        if policy_uri is not None:
            self.policy_uri = policy_uri
        if post_logout_redirect_uris is not None:
            self.post_logout_redirect_uris = post_logout_redirect_uris
        if redirect_uris is not None:
            self.redirect_uris = redirect_uris
        if wildcard_redirect is not None:
            self.wildcard_redirect = wildcard_redirect
        if response_types is not None:
            self.response_types = response_types
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if tos_uri is not None:
            self.tos_uri = tos_uri
        if jwks is not None:
            self.jwks = jwks

    @property
    def application_type(self):
        """Gets the application_type of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The application_type of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: OpenIdConnectApplicationType
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """Sets the application_type of this OpenIdConnectApplicationSettingsClient.


        :param application_type: The application_type of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: OpenIdConnectApplicationType
        """

        self._application_type = application_type

    @property
    def client_uri(self):
        """Gets the client_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The client_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: str
        """
        return self._client_uri

    @client_uri.setter
    def client_uri(self, client_uri):
        """Sets the client_uri of this OpenIdConnectApplicationSettingsClient.


        :param client_uri: The client_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: str
        """

        self._client_uri = client_uri

    @property
    def consent_method(self):
        """Gets the consent_method of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The consent_method of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: OpenIdConnectApplicationConsentMethod
        """
        return self._consent_method

    @consent_method.setter
    def consent_method(self, consent_method):
        """Sets the consent_method of this OpenIdConnectApplicationSettingsClient.


        :param consent_method: The consent_method of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: OpenIdConnectApplicationConsentMethod
        """

        self._consent_method = consent_method

    @property
    def grant_types(self):
        """Gets the grant_types of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The grant_types of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: list[OAuthGrantType]
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        """Sets the grant_types of this OpenIdConnectApplicationSettingsClient.


        :param grant_types: The grant_types of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: list[OAuthGrantType]
        """

        self._grant_types = grant_types

    @property
    def initiate_login_uri(self):
        """Gets the initiate_login_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The initiate_login_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: str
        """
        return self._initiate_login_uri

    @initiate_login_uri.setter
    def initiate_login_uri(self, initiate_login_uri):
        """Sets the initiate_login_uri of this OpenIdConnectApplicationSettingsClient.


        :param initiate_login_uri: The initiate_login_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: str
        """

        self._initiate_login_uri = initiate_login_uri

    @property
    def issuer_mode(self):
        """Gets the issuer_mode of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The issuer_mode of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: OpenIdConnectApplicationIssuerMode
        """
        return self._issuer_mode

    @issuer_mode.setter
    def issuer_mode(self, issuer_mode):
        """Sets the issuer_mode of this OpenIdConnectApplicationSettingsClient.


        :param issuer_mode: The issuer_mode of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: OpenIdConnectApplicationIssuerMode
        """

        self._issuer_mode = issuer_mode

    @property
    def idp_initiated_login(self):
        """Gets the idp_initiated_login of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The idp_initiated_login of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: OpenIdConnectApplicationIdpInitiatedLogin
        """
        return self._idp_initiated_login

    @idp_initiated_login.setter
    def idp_initiated_login(self, idp_initiated_login):
        """Sets the idp_initiated_login of this OpenIdConnectApplicationSettingsClient.


        :param idp_initiated_login: The idp_initiated_login of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: OpenIdConnectApplicationIdpInitiatedLogin
        """

        self._idp_initiated_login = idp_initiated_login

    @property
    def logo_uri(self):
        """Gets the logo_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The logo_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: str
        """
        return self._logo_uri

    @logo_uri.setter
    def logo_uri(self, logo_uri):
        """Sets the logo_uri of this OpenIdConnectApplicationSettingsClient.


        :param logo_uri: The logo_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: str
        """

        self._logo_uri = logo_uri

    @property
    def policy_uri(self):
        """Gets the policy_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The policy_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: str
        """
        return self._policy_uri

    @policy_uri.setter
    def policy_uri(self, policy_uri):
        """Sets the policy_uri of this OpenIdConnectApplicationSettingsClient.


        :param policy_uri: The policy_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: str
        """

        self._policy_uri = policy_uri

    @property
    def post_logout_redirect_uris(self):
        """Gets the post_logout_redirect_uris of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The post_logout_redirect_uris of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: list[str]
        """
        return self._post_logout_redirect_uris

    @post_logout_redirect_uris.setter
    def post_logout_redirect_uris(self, post_logout_redirect_uris):
        """Sets the post_logout_redirect_uris of this OpenIdConnectApplicationSettingsClient.


        :param post_logout_redirect_uris: The post_logout_redirect_uris of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: list[str]
        """

        self._post_logout_redirect_uris = post_logout_redirect_uris

    @property
    def redirect_uris(self):
        """Gets the redirect_uris of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The redirect_uris of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: list[str]
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """Sets the redirect_uris of this OpenIdConnectApplicationSettingsClient.


        :param redirect_uris: The redirect_uris of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: list[str]
        """

        self._redirect_uris = redirect_uris

    @property
    def wildcard_redirect(self):
        """Gets the wildcard_redirect of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The wildcard_redirect of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: str
        """
        return self._wildcard_redirect

    @wildcard_redirect.setter
    def wildcard_redirect(self, wildcard_redirect):
        """Sets the wildcard_redirect of this OpenIdConnectApplicationSettingsClient.


        :param wildcard_redirect: The wildcard_redirect of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: str
        """

        self._wildcard_redirect = wildcard_redirect

    @property
    def response_types(self):
        """Gets the response_types of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The response_types of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: list[OAuthResponseType]
        """
        return self._response_types

    @response_types.setter
    def response_types(self, response_types):
        """Sets the response_types of this OpenIdConnectApplicationSettingsClient.


        :param response_types: The response_types of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: list[OAuthResponseType]
        """

        self._response_types = response_types

    @property
    def refresh_token(self):
        """Gets the refresh_token of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The refresh_token of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: OpenIdConnectApplicationSettingsRefreshToken
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this OpenIdConnectApplicationSettingsClient.


        :param refresh_token: The refresh_token of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: OpenIdConnectApplicationSettingsRefreshToken
        """

        self._refresh_token = refresh_token

    @property
    def tos_uri(self):
        """Gets the tos_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The tos_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: str
        """
        return self._tos_uri

    @tos_uri.setter
    def tos_uri(self, tos_uri):
        """Sets the tos_uri of this OpenIdConnectApplicationSettingsClient.


        :param tos_uri: The tos_uri of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: str
        """

        self._tos_uri = tos_uri

    @property
    def jwks(self):
        """Gets the jwks of this OpenIdConnectApplicationSettingsClient.  # noqa: E501


        :return: The jwks of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :rtype: OpenIdConnectApplicationSettingsClientKeys
        """
        return self._jwks

    @jwks.setter
    def jwks(self, jwks):
        """Sets the jwks of this OpenIdConnectApplicationSettingsClient.


        :param jwks: The jwks of this OpenIdConnectApplicationSettingsClient.  # noqa: E501
        :type: OpenIdConnectApplicationSettingsClientKeys
        """

        self._jwks = jwks

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
        if issubclass(OpenIdConnectApplicationSettingsClient, dict):
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
        if not isinstance(other, OpenIdConnectApplicationSettingsClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
