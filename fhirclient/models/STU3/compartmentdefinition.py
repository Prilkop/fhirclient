#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/CompartmentDefinition) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class CompartmentDefinition(domainresource.DomainResource):
    """ Compartment Definition for a resource.
    
    A compartment definition that defines how resources are accessed on a
    server.
    """
    
    resource_type = "CompartmentDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Logical URI to reference this compartment definition (globally
        unique).
        Type `str`. """
        
        self.name = None
        """ Name for this compartment definition (computer friendly).
        Type `str`. """
        
        self.title = None
        """ Name for this compartment definition (human friendly).
        Type `str`. """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the compartment definition.
        Type `str`. """
        
        self.purpose = None
        """ Why this compartment definition is defined.
        Type `str`. """
        
        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for compartment definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Patient | Encounter | RelatedPerson | Practitioner | Device.
        Type `str`. """
        
        self.search = None
        """ Whether the search syntax is supported.
        Type `bool`. """
        
        self.resource = None
        """ How a resource is related to the compartment.
        List of `CompartmentDefinitionResource` items (represented as `dict` in JSON). """
        
        super(CompartmentDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompartmentDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", str, False, None, True),
            ("search", "search", bool, False, None, True),
            ("resource", "resource", CompartmentDefinitionResource, True, None, False),
        ])
        return js


from . import backboneelement

class CompartmentDefinitionResource(backboneelement.BackboneElement):
    """ How a resource is related to the compartment.
    
    Information about how a resource is related to the compartment.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Name of resource type.
        Type `str`. """
        
        self.param = None
        """ Search Parameter Name, or chained parameters.
        List of `str` items. """
        
        self.documentation = None
        """ Additional documentation about the resource and compartment.
        Type `str`. """
        
        super(CompartmentDefinitionResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompartmentDefinitionResource, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("param", "param", str, True, None, False),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
