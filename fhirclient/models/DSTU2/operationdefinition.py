#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class OperationDefinition(domainresource.DomainResource):
    """ Definition of an operation or a named query.
    
    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """
    
    resource_type = "OperationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Logical URL to reference this operation definition.
        Type `str`. """
        
        self.version = None
        """ Logical id for this version of the operation definition.
        Type `str`. """
        
        self.name = None
        """ Informal name for this operation.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.kind = None
        """ operation | query.
        Type `str`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `OperationDefinitionContact` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date for this version of the operation definition.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the operation.
        Type `str`. """
        
        self.requirements = None
        """ Why is this needed?.
        Type `str`. """
        
        self.idempotent = None
        """ Whether content is unchanged by operation.
        Type `bool`. """
        
        self.code = None
        """ Name used to invoke the operation.
        Type `str`. """
        
        self.notes = None
        """ Additional information about use.
        Type `str`. """
        
        self.base = None
        """ Marks this as a profile of the base.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.system = None
        """ Invoke at the system level?.
        Type `bool`. """
        
        self.type = None
        """ Invoke at resource level for these type.
        List of `str` items. """
        
        self.instance = None
        """ Invoke on an instance?.
        Type `bool`. """
        
        self.parameter = None
        """ Parameters for the operation/query.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        
        super(OperationDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("status", "status", str, False, None, True),
            ("kind", "kind", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", OperationDefinitionContact, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("idempotent", "idempotent", bool, False, None, False),
            ("code", "code", str, False, None, True),
            ("notes", "notes", str, False, None, False),
            ("base", "base", fhirreference.FHIRReference, False, None, False),
            ("system", "system", bool, False, None, True),
            ("type", "type", str, True, None, False),
            ("instance", "instance", bool, False, None, True),
            ("parameter", "parameter", OperationDefinitionParameter, True, None, False),
        ])
        return js


from . import backboneelement

class OperationDefinitionContact(backboneelement.BackboneElement):
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
        
        super(OperationDefinitionContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class OperationDefinitionParameter(backboneelement.BackboneElement):
    """ Parameters for the operation/query.
    
    The parameters for the operation/query.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name in Parameters.parameter.name or in URL.
        Type `str`. """
        
        self.use = None
        """ in | out.
        Type `str`. """
        
        self.min = None
        """ Minimum Cardinality.
        Type `int`. """
        
        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `str`. """
        
        self.documentation = None
        """ Description of meaning/use.
        Type `str`. """
        
        self.type = None
        """ What type this parameter has.
        Type `str`. """
        
        self.profile = None
        """ Profile on the type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.binding = None
        """ ValueSet details if this is coded.
        Type `OperationDefinitionParameterBinding` (represented as `dict` in JSON). """
        
        self.part = None
        """ Parts of a Tuple Parameter.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        
        super(OperationDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("use", "use", str, False, None, True),
            ("min", "min", int, False, None, True),
            ("max", "max", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("type", "type", str, False, None, False),
            ("profile", "profile", fhirreference.FHIRReference, False, None, False),
            ("binding", "binding", OperationDefinitionParameterBinding, False, None, False),
            ("part", "part", OperationDefinitionParameter, True, None, False),
        ])
        return js


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.strength = None
        """ required | extensible | preferred | example.
        Type `str`. """
        
        self.valueSetUri = None
        """ Source of value set.
        Type `str`. """
        
        self.valueSetReference = None
        """ Source of value set.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(OperationDefinitionParameterBinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameterBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", str, False, None, True),
            ("valueSetUri", "valueSetUri", str, False, "valueSet", True),
            ("valueSetReference", "valueSetReference", fhirreference.FHIRReference, False, "valueSet", True),
        ])
        return js


import sys
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
