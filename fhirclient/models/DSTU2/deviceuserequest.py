#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceUseRequest) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class DeviceUseRequest(domainresource.DomainResource):
    """ A request for a patient to use or be given a medical device.
    
    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    
    resource_type = "DeviceUseRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySiteCodeableConcept = None
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySiteReference = None
        """ Target body site.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | planned | requested | received | accepted | in-progress
        | completed | suspended | rejected | aborted.
        Type `str`. """
        
        self.device = None
        """ Device requested.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter motivating request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Request identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Notes or comments.
        List of `str` items. """
        
        self.prnReason = None
        """ PRN.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.orderedOn = None
        """ When ordered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recordedOn = None
        """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subject = None
        """ Focus of request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ Schedule for use.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        """ Schedule for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ Schedule for use.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.priority = None
        """ routine | urgent | stat | asap.
        Type `str`. """
        
        super(DeviceUseRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceUseRequest, self).elementProperties()
        js.extend([
            ("bodySiteCodeableConcept", "bodySiteCodeableConcept", codeableconcept.CodeableConcept, False, "bodySite", False),
            ("bodySiteReference", "bodySiteReference", fhirreference.FHIRReference, False, "bodySite", False),
            ("status", "status", str, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("indication", "indication", codeableconcept.CodeableConcept, True, None, False),
            ("notes", "notes", str, True, None, False),
            ("prnReason", "prnReason", codeableconcept.CodeableConcept, True, None, False),
            ("orderedOn", "orderedOn", fhirdate.FHIRDate, False, None, False),
            ("recordedOn", "recordedOn", fhirdate.FHIRDate, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("priority", "priority", str, False, None, False),
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
