#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ProcedureRequest) on 2022-04-28.
#  2022, SMART Health IT.


from . import domainresource

class ProcedureRequest(domainresource.DomainResource):
    """ A request for a procedure to be performed.
    
    A request for a procedure to be performed. May be a proposal or an order.
    """
    
    resource_type = "ProcedureRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique identifier for the request.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who the procedure should be done to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.code = None
        """ What procedure to perform.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ What part of body to perform on.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Why procedure should occur.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why procedure should occur.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.scheduledDateTime = None
        """ When procedure should occur.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.scheduledPeriod = None
        """ When procedure should occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scheduledTiming = None
        """ When procedure should occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter request created during.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who should perform the procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | draft | requested | received | accepted | in-progress |
        completed | suspended | rejected | aborted.
        Type `str`. """
        
        self.notes = None
        """ Additional information about desired procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.asNeededBoolean = None
        """ Preconditions for procedure.
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Preconditions for procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.orderedOn = None
        """ When request was created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.orderer = None
        """ Who made request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | stat | asap.
        Type `str`. """
        
        super(ProcedureRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedureRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False, "reason", False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, "reason", False),
            ("scheduledDateTime", "scheduledDateTime", fhirdate.FHIRDate, False, "scheduled", False),
            ("scheduledPeriod", "scheduledPeriod", period.Period, False, "scheduled", False),
            ("scheduledTiming", "scheduledTiming", timing.Timing, False, "scheduled", False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("status", "status", ProcedureRequestStatus.str, False, None, False),
            ("notes", "notes", annotation.Annotation, True, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("orderedOn", "orderedOn", fhirdate.FHIRDate, False, None, False),
            ("orderer", "orderer", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", ProcedureRequestPriority.str, False, None, False),
        ])
        return js


import sys
try:
    from . import ProcedureRequestPriority
except ImportError:
    ProcedureRequestPriority = sys.modules[__package__ + '.ProcedureRequestPriority']
try:
    from . import ProcedureRequestStatus
except ImportError:
    ProcedureRequestStatus = sys.modules[__package__ + '.ProcedureRequestStatus']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
