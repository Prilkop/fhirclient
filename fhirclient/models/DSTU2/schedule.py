#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Schedule) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class Schedule(domainresource.DomainResource):
    """ A container for slot(s) of time that may be available for booking
    appointments.
    """
    
    resource_type = "Schedule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.type = None
        """ The schedule type can be used for the categorization of healthcare
        services or other appointment types.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor = None
        """ The resource this Schedule resource is providing availability
        information for. These are expected to usually be one of
        HealthcareService, Location, Practitioner, Device, Patient or
        RelatedPerson.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.planningHorizon = None
        """ The period of time that the slots that are attached to this
        Schedule resource cover (even if none exist). These  cover the
        amount of time that an organization's planning horizon; the
        interval for which they are currently accepting appointments. This
        does not define a "template" for planning outside these dates.
        Type `Period` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Comments on the availability to describe any extended information.
        Such as custom constraints on the slot(s) that may be associated.
        Type `str`. """
        
        super(Schedule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Schedule, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("planningHorizon", "planningHorizon", period.Period, False, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
