#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Order) on 2022-04-28.
#  2022, SMART Health IT.


from . import domainresource

class Order(domainresource.DomainResource):
    """ A request to perform an action.
    """
    
    resource_type = "Order"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.date = None
        """ When the order was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subject = None
        """ Patient this order is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        """ Who initiated the order.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.target = None
        """ Who is intended to fulfill the order.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Text - why the order was made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Text - why the order was made.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.when = None
        """ When order should be fulfilled.
        Type `OrderWhen` (represented as `dict` in JSON). """
        
        self.detail = None
        """ What action is being ordered.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(Order, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Order, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False, "reason", False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, "reason", False),
            ("when", "when", OrderWhen, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, True),
        ])
        return js


from . import backboneelement

class OrderWhen(backboneelement.BackboneElement):
    """ When order should be fulfilled.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code specifies when request should be done. The code may simply be
        a priority code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ A formal schedule.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(OrderWhen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OrderWhen, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("schedule", "schedule", timing.Timing, False, None, False),
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
