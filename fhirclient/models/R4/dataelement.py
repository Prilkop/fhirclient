#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DataElement) on 2022-04-28.
#  2022, SMART Health IT.


from . import domainresource

class DataElement(domainresource.DomainResource):
    """ Resource data element.
    
    The formal description of a single piece of information that can be
    gathered and reported.
    """
    
    resource_type = "DataElement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Globally unique logical id for data element.
        Type `str`. """
        
        self.identifier = None
        """ Logical id to reference this data element.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the data element.
        Type `str`. """
        
        self.name = None
        """ Descriptive label for this element definition.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `DataElementContact` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date for this version of the data element.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.stringency = None
        """ comparable | fully-specified | equivalent | convertable | scaleable
        | flexible.
        Type `str`. """
        
        self.mapping = None
        """ External specification mapped to.
        List of `DataElementMapping` items (represented as `dict` in JSON). """
        
        self.element = None
        """ Definition of element.
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(DataElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataElement, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("status", "status", ConformanceResourceStatus.str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", DataElementContact, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("stringency", "stringency", DataElementStringency.str, False, None, False),
            ("mapping", "mapping", DataElementMapping, True, None, False),
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
        ])
        return js


from . import backboneelement

class DataElementContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(DataElementContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataElementContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class DataElementMapping(backboneelement.BackboneElement):
    """ External specification mapped to.
    
    Identifies a specification (other than a terminology) that the elements
    which make up the DataElement have some correspondence with.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identity = None
        """ Internal id when this mapping is used.
        Type `str`. """
        
        self.uri = None
        """ Identifies what this mapping refers to.
        Type `str`. """
        
        self.name = None
        """ Names what this mapping refers to.
        Type `str`. """
        
        self.comments = None
        """ Versions, Issues, Scope limitations etc..
        Type `str`. """
        
        super(DataElementMapping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataElementMapping, self).elementProperties()
        js.extend([
            ("identity", "identity", str, False, None, True),
            ("uri", "uri", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("comments", "comments", str, False, None, False),
        ])
        return js


import sys
try:
    from . import ConformanceResourceStatus
except ImportError:
    ConformanceResourceStatus = sys.modules[__package__ + '.ConformanceResourceStatus']
try:
    from . import DataElementStringency
except ImportError:
    DataElementStringency = sys.modules[__package__ + '.DataElementStringency']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import elementdefinition
except ImportError:
    elementdefinition = sys.modules[__package__ + '.elementdefinition']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
