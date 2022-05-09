#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ProcessResponse) on 2022-04-28.
#  2022, SMART Health IT.


from . import domainresource

class ProcessResponse(domainresource.DomainResource):
    """ ProcessResponse resource.
    
    This resource provides processing status, errors and notes from the
    processing of a resource.
    """
    
    resource_type = "ProcessResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ Processing outcome.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.organization = None
        """ Authoring Organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible Practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.form = None
        """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.notes = None
        """ Notes.
        List of `ProcessResponseNotes` items (represented as `dict` in JSON). """
        
        self.error = None
        """ Error code.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(ProcessResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcessResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", coding.Coding, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False, None, False),
            ("form", "form", coding.Coding, False, None, False),
            ("notes", "notes", ProcessResponseNotes, True, None, False),
            ("error", "error", coding.Coding, True, None, False),
        ])
        return js


from . import backboneelement

class ProcessResponseNotes(backboneelement.BackboneElement):
    """ Notes.
    
    Suite of processing note or additional requirements is the processing has
    been held.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.text = None
        """ Notes text.
        Type `str`. """
        
        super(ProcessResponseNotes, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcessResponseNotes, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


import sys
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
