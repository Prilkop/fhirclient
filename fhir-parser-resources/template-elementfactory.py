#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR {{ info.version }} on {{ info.date }}.
#  {{ info.year }}, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    _resource_class_mapping = {}

    @classmethod
    def _init_resource_class_mapping(cls):
        {%- macro import_list() %}{% for klass in classes %}{% if klass.resource_type %}{{ klass.name }}, {% endif %}{% endfor %}Element{% endmacro %}
        from . import {{ import_list() | wordwrap(125) | replace("\n", " \\\n                      ")}}

        cls._resource_class_mapping = {
{%- for klass in classes %}{% if klass.resource_type %}
            "{{ klass.resource_type }}": {{ klass.name }},
{%- endif %}{% endfor %}
            None: Element
        }

    @classmethod
    def get_resource_class(cls, resource_type):
        """ Return a resource class for the type correlating to "resource_type".

        :param str resource_type: The name/type of the resource to instantiate
        :returns: A resource class for the respective type or `Element`
        """
        if not cls._resource_class_mapping:
            cls._init_resource_class_mapping()

        return cls._resource_class_mapping.get(resource_type, cls._resource_class_mapping[None])

    @classmethod
    def instantiate(cls, resource_type, jsondict):
        """ Instantiate a resource of the type correlating to "resource_type".

        :param str resource_type: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :returns: A resource of the respective type or `Element`
        """
        klass = cls.get_resource_class(resource_type)
        return klass(jsondict)

    @classmethod
    def read_from(cls, path, server):
        """ Requests data from the given REST path on the server and creates
        an instance of based on the path.

        :param str path: The REST path to read from
        :param FHIRServer server: An instance of a FHIR server or compatible class
        :returns: An instance of the receiving class
        """
        if not path:
            raise Exception("Cannot read resource without REST path")
        if server is None:
            raise Exception("Cannot read resource without server instance")

        resource_type = path.split('/')[0]
        klass = cls.get_resource_class(resource_type)
        return klass.read_from(path, server)


