#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DetectedIssue) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class DetectedIssue(domainresource.DomainResource):
    """ Clinical issue with action.
    
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """
    
    resource_type = "DetectedIssue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.patient = None
        """ Associated patient.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.category = None
        """ Issue Category, e.g. drug-drug, duplicate therapy, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.severity = None
        """ high | moderate | low.
        Type `str`. """
        
        self.implicated = None
        """ Problem resource.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Description and context.
        Type `str`. """
        
        self.date = None
        """ When identified.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        """ The provider or device that identified the issue.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique id for the detected issue.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Authority for issue.
        Type `str`. """
        
        self.mitigation = None
        """ Step taken to address.
        List of `DetectedIssueMitigation` items (represented as `dict` in JSON). """
        
        super(DetectedIssue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssue, self).elementProperties()
        js.extend([
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("implicated", "implicated", fhirreference.FHIRReference, True, None, False),
            ("detail", "detail", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("mitigation", "mitigation", DetectedIssueMitigation, True, None, False),
        ])
        return js


from . import backboneelement

class DetectedIssueMitigation(backboneelement.BackboneElement):
    """ Step taken to address.
    
    Indicates an action that has been taken or is committed to to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ What mitigation?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ Date committed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        """ Who is committing?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DetectedIssueMitigation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssueMitigation, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
