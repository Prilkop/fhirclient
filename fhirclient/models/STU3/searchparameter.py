#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class SearchParameter(domainresource.DomainResource):
    """ Search Parameter for a resource.
    
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """
    
    resource_type = "SearchParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Logical URI to reference this search parameter (globally unique).
        Type `str`. """
        
        self.version = None
        """ Business version of the search parameter.
        Type `str`. """
        
        self.name = None
        """ Name for this search parameter (computer friendly).
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
        
        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for search parameter (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this search parameter is defined.
        Type `str`. """
        
        self.code = None
        """ Code used in URL.
        Type `str`. """
        
        self.base = None
        """ The resource type(s) this search parameter applies to.
        List of `str` items. """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri.
        Type `str`. """
        
        self.derivedFrom = None
        """ Original Definition for the search parameter.
        Type `str`. """
        
        self.description = None
        """ Natural language description of the search parameter.
        Type `str`. """
        
        self.expression = None
        """ FHIRPath expression that extracts the values.
        Type `str`. """
        
        self.xpath = None
        """ XPath that extracts the values.
        Type `str`. """
        
        self.xpathUsage = None
        """ normal | phonetic | nearby | distance | other.
        Type `str`. """
        
        self.target = None
        """ Types of resource (if a resource reference).
        List of `str` items. """
        
        self.comparator = None
        """ eq | ne | gt | lt | ge | le | sa | eb | ap.
        List of `str` items. """
        
        self.modifier = None
        """ missing | exact | contains | not | text | in | not-in | below |
        above | type.
        List of `str` items. """
        
        self.chain = None
        """ Chained names supported.
        List of `str` items. """
        
        self.component = None
        """ For Composite resources to define the parts.
        List of `SearchParameterComponent` items (represented as `dict` in JSON). """
        
        super(SearchParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("code", "code", str, False, None, True),
            ("base", "base", str, True, None, True),
            ("type", "type", str, False, None, True),
            ("derivedFrom", "derivedFrom", str, False, None, False),
            ("description", "description", str, False, None, True),
            ("expression", "expression", str, False, None, False),
            ("xpath", "xpath", str, False, None, False),
            ("xpathUsage", "xpathUsage", str, False, None, False),
            ("target", "target", str, True, None, False),
            ("comparator", "comparator", str, True, None, False),
            ("modifier", "modifier", str, True, None, False),
            ("chain", "chain", str, True, None, False),
            ("component", "component", SearchParameterComponent, True, None, False),
        ])
        return js


from . import backboneelement

class SearchParameterComponent(backboneelement.BackboneElement):
    """ For Composite resources to define the parts.
    
    Used to define the parts of a composite search parameter.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ Defines how the part works.
        Type `FHIRReference` referencing `SearchParameter` (represented as `dict` in JSON). """
        
        self.expression = None
        """ Subexpression relative to main expression.
        Type `str`. """
        
        super(SearchParameterComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend([
            ("definition", "definition", fhirreference.FHIRReference, False, None, True),
            ("expression", "expression", str, False, None, True),
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
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
