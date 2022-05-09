#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ConceptMap) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class ConceptMap(domainresource.DomainResource):
    """ A map from one set of concepts to one or more other concepts.
    
    A statement of relationships from one set of concepts to one or more other
    concepts - either code systems or data elements, or classes in class
    models.
    """
    
    resource_type = "ConceptMap"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Globally unique logical id for concept map.
        Type `str`. """
        
        self.identifier = None
        """ Additional identifier for the concept map.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the concept map.
        Type `str`. """
        
        self.name = None
        """ Informal name for this concept map.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ConceptMapContact` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Human language description of the concept map.
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.requirements = None
        """ Why needed.
        Type `str`. """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.sourceUri = None
        """ Identifies the source of the concepts which are being mapped.
        Type `str`. """
        
        self.sourceReference = None
        """ Identifies the source of the concepts which are being mapped.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.targetUri = None
        """ Provides context to the mappings.
        Type `str`. """
        
        self.targetReference = None
        """ Provides context to the mappings.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.element = None
        """ Mappings for a concept from the source set.
        List of `ConceptMapElement` items (represented as `dict` in JSON). """
        
        super(ConceptMap, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMap, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ConceptMapContact, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("sourceUri", "sourceUri", str, False, "source", True),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", True),
            ("targetUri", "targetUri", str, False, "target", True),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False, "target", True),
            ("element", "element", ConceptMapElement, True, None, False),
        ])
        return js


from . import backboneelement

class ConceptMapContact(backboneelement.BackboneElement):
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
        
        super(ConceptMapContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class ConceptMapElement(backboneelement.BackboneElement):
    """ Mappings for a concept from the source set.
    
    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeSystem = None
        """ Code System (if value set crosses code systems).
        Type `str`. """
        
        self.code = None
        """ Identifies element being mapped.
        Type `str`. """
        
        self.target = None
        """ Concept in target system for element.
        List of `ConceptMapElementTarget` items (represented as `dict` in JSON). """
        
        super(ConceptMapElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapElement, self).elementProperties()
        js.extend([
            ("codeSystem", "codeSystem", str, False, None, False),
            ("code", "code", str, False, None, False),
            ("target", "target", ConceptMapElementTarget, True, None, False),
        ])
        return js


class ConceptMapElementTarget(backboneelement.BackboneElement):
    """ Concept in target system for element.
    
    A concept from the target value set that this concept maps to.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeSystem = None
        """ System of the target (if necessary).
        Type `str`. """
        
        self.code = None
        """ Code that identifies the target element.
        Type `str`. """
        
        self.equivalence = None
        """ equivalent | equal | wider | subsumes | narrower | specializes |
        inexact | unmatched | disjoint.
        Type `str`. """
        
        self.comments = None
        """ Description of status/issues in mapping.
        Type `str`. """
        
        self.dependsOn = None
        """ Other elements required for this mapping (from context).
        List of `ConceptMapElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        self.product = None
        """ Other concepts that this mapping also produces.
        List of `ConceptMapElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        super(ConceptMapElementTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapElementTarget, self).elementProperties()
        js.extend([
            ("codeSystem", "codeSystem", str, False, None, False),
            ("code", "code", str, False, None, False),
            ("equivalence", "equivalence", str, False, None, True),
            ("comments", "comments", str, False, None, False),
            ("dependsOn", "dependsOn", ConceptMapElementTargetDependsOn, True, None, False),
            ("product", "product", ConceptMapElementTargetDependsOn, True, None, False),
        ])
        return js


class ConceptMapElementTargetDependsOn(backboneelement.BackboneElement):
    """ Other elements required for this mapping (from context).
    
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        """ Reference to element/field/ValueSet mapping depends on.
        Type `str`. """
        
        self.codeSystem = None
        """ Code System (if necessary).
        Type `str`. """
        
        self.code = None
        """ Value of the referenced element.
        Type `str`. """
        
        super(ConceptMapElementTargetDependsOn, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapElementTargetDependsOn, self).elementProperties()
        js.extend([
            ("element", "element", str, False, None, True),
            ("codeSystem", "codeSystem", str, False, None, True),
            ("code", "code", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
