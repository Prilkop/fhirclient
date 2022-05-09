#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ None.
    
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    
    resource_type = "DeviceUseStatement"
    
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
        
        self.whenUsed = None
        """ None.
        Type `Period` (represented as `dict` in JSON). """
        
        self.device = None
        """ None.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ None.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ None.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ None.
        List of `str` items. """
        
        self.recordedOn = None
        """ None.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subject = None
        """ None.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ None.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        """ None.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ None.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(DeviceUseStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("bodySiteCodeableConcept", "bodySiteCodeableConcept", codeableconcept.CodeableConcept, False, "bodySite", False),
            ("bodySiteReference", "bodySiteReference", fhirreference.FHIRReference, False, "bodySite", False),
            ("whenUsed", "whenUsed", period.Period, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("indication", "indication", codeableconcept.CodeableConcept, True, None, False),
            ("notes", "notes", str, True, None, False),
            ("recordedOn", "recordedOn", fhirdate.FHIRDate, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
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
