#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Coverage) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan.
    
    Financial instrument which may be used to pay for or reimburse health care
    products and services.
    """
    
    resource_type = "Coverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.issuer = None
        """ An identifier for the plan issuer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.bin = None
        """ BIN Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.period = None
        """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of coverage.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subscriberId = None
        """ Subscriber ID.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ The primary coverage ID.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.group = None
        """ An identifier for the group.
        Type `str`. """
        
        self.plan = None
        """ An identifier for the plan.
        Type `str`. """
        
        self.subPlan = None
        """ An identifier for the subsection of the plan.
        Type `str`. """
        
        self.dependent = None
        """ The dependent number.
        Type `int`. """
        
        self.sequence = None
        """ The plan instance or sequence counter.
        Type `int`. """
        
        self.subscriber = None
        """ Plan holder information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.network = None
        """ Insurer network.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.contract = None
        """ Contract details.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, False),
            ("bin", "bin", identifier.Identifier, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
            ("subscriberId", "subscriberId", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("group", "group", str, False, None, False),
            ("plan", "plan", str, False, None, False),
            ("subPlan", "subPlan", str, False, None, False),
            ("dependent", "dependent", int, False, None, False),
            ("sequence", "sequence", int, False, None, False),
            ("subscriber", "subscriber", fhirreference.FHIRReference, False, None, False),
            ("network", "network", identifier.Identifier, False, None, False),
            ("contract", "contract", fhirreference.FHIRReference, True, None, False),
        ])
        return js


import sys
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
