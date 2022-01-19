# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.9.2
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from okta.swagger_api_client import ApiClient


class Template(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_sms_template(self, body, **kwargs):  # noqa: E501
        """Add SMS Template  # noqa: E501

        Adds a new custom SMS template to your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_sms_template(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SmsTemplate body: (required)
        :return: SmsTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_sms_template_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_sms_template_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_sms_template_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add SMS Template  # noqa: E501

        Adds a new custom SMS template to your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_sms_template_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SmsTemplate body: (required)
        :return: SmsTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_sms_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_sms_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/templates/sms', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmsTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_sms_template(self, template_id, **kwargs):  # noqa: E501
        """Remove SMS Template  # noqa: E501

        Removes an SMS template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sms_template(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_sms_template_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_sms_template_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def delete_sms_template_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Remove SMS Template  # noqa: E501

        Removes an SMS template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sms_template_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_sms_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `delete_sms_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['templateId'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/templates/sms/{templateId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sms_template(self, template_id, **kwargs):  # noqa: E501
        """Get SMS Template  # noqa: E501

        Fetches a specific template by `id`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sms_template(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :return: SmsTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sms_template_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sms_template_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def get_sms_template_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Get SMS Template  # noqa: E501

        Fetches a specific template by `id`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sms_template_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :return: SmsTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sms_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `get_sms_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['templateId'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/templates/sms/{templateId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmsTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_sms_templates(self, **kwargs):  # noqa: E501
        """List SMS Templates  # noqa: E501

        Enumerates custom SMS templates in your organization. A subset of templates can be returned that match a template type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_sms_templates(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SmsTemplateType template_type:
        :return: list[SmsTemplate]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_sms_templates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_sms_templates_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_sms_templates_with_http_info(self, **kwargs):  # noqa: E501
        """List SMS Templates  # noqa: E501

        Enumerates custom SMS templates in your organization. A subset of templates can be returned that match a template type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_sms_templates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SmsTemplateType template_type:
        :return: list[SmsTemplate]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_sms_templates" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_type' in params:
            query_params.append(('templateType', params['template_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/templates/sms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SmsTemplate]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def partial_update_sms_template(self, template_id, body, **kwargs):  # noqa: E501
        """Partial SMS Template Update  # noqa: E501

        Updates only some of the SMS template properties:  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_sms_template(template_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param SmsTemplate body: (required)
        :return: SmsTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.partial_update_sms_template_with_http_info(template_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.partial_update_sms_template_with_http_info(template_id, body, **kwargs)  # noqa: E501
            return data

    def partial_update_sms_template_with_http_info(self, template_id, body, **kwargs):  # noqa: E501
        """Partial SMS Template Update  # noqa: E501

        Updates only some of the SMS template properties:  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_sms_template_with_http_info(template_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param SmsTemplate body: (required)
        :return: SmsTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id''body', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_update_sms_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `partial_update_sms_template`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `partial_update_sms_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['templateId'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/templates/sms/{templateId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmsTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_sms_template(self, template_id, body, **kwargs):  # noqa: E501
        """Update SMS Template  # noqa: E501

        Updates the SMS template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_sms_template(template_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param SmsTemplate body: (required)
        :return: SmsTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_sms_template_with_http_info(template_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_sms_template_with_http_info(template_id, body, **kwargs)  # noqa: E501
            return data

    def update_sms_template_with_http_info(self, template_id, body, **kwargs):  # noqa: E501
        """Update SMS Template  # noqa: E501

        Updates the SMS template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_sms_template_with_http_info(template_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param SmsTemplate body: (required)
        :return: SmsTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id''body', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_sms_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `update_sms_template`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_sms_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['templateId'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/templates/sms/{templateId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmsTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
