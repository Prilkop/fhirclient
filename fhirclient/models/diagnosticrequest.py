#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10210 (http://hl7.org/fhir/StructureDefinition/DiagnosticRequest) on 2016-11-17.
#  2016, SMART Health IT.


from . import domainresource

class DiagnosticRequest(domainresource.DomainResource):
    """ A request for a diagnostic service.
    
    A record of a request for a diagnostic investigation service to be
    performed.
    """
    
    resource_name = "DiagnosticRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authored = None
        """ Date request signed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.code = None
        """ What’s being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter or Episode during which request was created.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.definition = None
        """ Protocol or definition.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifiers assigned to this order.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When testing should occur.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When testing should occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ When testing should occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Requested perfomer.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, Device, RelatedPerson` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ Performer role.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Explanation/Justification for test.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.relevantHistory = None
        """ Request provenance.
        List of `FHIRReference` items referencing `Provenance` (represented as `dict` in JSON). """
        
        self.replaces = None
        """ What request replaces.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Who/what is requesting diagnostics.
        Type `FHIRReference` referencing `Device, Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.requisition = None
        """ Identifier of composite request.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.stage = None
        """ proposal | plan | original-order | reflex-order.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | suspended | completed | entered-in-error |
        cancelled.
        Type `str`. """
        
        self.subject = None
        """ Individual the test is ordered for.
        Type `FHIRReference` referencing `Patient, Group, Location, Device` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ Additional clinical information.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(DiagnosticRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DiagnosticRequest, self).elementProperties()
        js.extend([
            ("authored", "authored", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("definition", "definition", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("requisition", "requisition", identifier.Identifier, False, None, False),
            ("stage", "stage", codeableconcept.CodeableConcept, False, None, True),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import timing